# -------------------------
# 🐍 main.py
# -------------------------
import os
import subprocess
import base64
import tempfile
import shlex
import sys
import yaml

def decode_kubeconfig(config):
    path = os.path.expanduser("~/.kube")
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/config", "w") as f:
        f.write(base64.b64decode(config).decode())

def write_values_file(content):
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml", mode="w")
    f.write(content)
    f.close()
    return f.name

def parse_multiline_flag(flag_value):
    return shlex.split(flag_value.strip()) if flag_value else []

def flag_if_true(env_key, flag_name=None):
    if os.getenv(env_key, "false").lower() == "true":
        return [f"--{flag_name or env_key.lower()}"]
    return []

def main():
    args = ["helm", "upgrade"]

    release = os.getenv("INPUT_RELEASE")
    chart = os.getenv("INPUT_CHART")
    if not release or not chart:
        print("❌ Error: release or chart missing")
        sys.exit(1)

    args += ["--install", release, chart]

    decode_kubeconfig(os.getenv("INPUT_KUBECONFIG"))

    # Direct value flags
    direct_flags = {
        "INPUT_NAMESPACE": "--namespace",
        "INPUT_VERSION": "--version",
        "INPUT_TIMEOUT": "--timeout",
        "INPUT_POST_RENDERER": "--post-renderer",
    }
    for env_var, flag in direct_flags.items():
        val = os.getenv(env_var)
        if val:
            args += [flag, val]

    # Boolean flags
    for bflag in [
        "ATOMIC", "WAIT", "INSTALL", "REUSE_VALUES", "RESET_VALUES",
        "DRY_RUN", "CLEANUP_ON_FAIL", "DEPENDENCY_UPDATE"
    ]:
        args += flag_if_true(f"INPUT_{bflag}", bflag.replace("_", "-").lower())

    # Multi value flags
    if values := os.getenv("INPUT_VALUES"):
        path = write_values_file(values)
        args += ["--values", path]

    for flag in ["SET", "SET_STRING", "SET_FILE"]:
        raw = os.getenv(f"INPUT_{flag}")
        if raw:
            for item in parse_multiline_flag(raw):
                args += [f"--{flag.lower().replace('_', '-')}", item]

    if pra := os.getenv("INPUT_POST_RENDERER_ARGS"):
        for item in parse_multiline_flag(pra):
            args += ["--post-renderer-args", item]

    print("🔧 Running:", " ".join(args))
    subprocess.run(args, check=True)

if __name__ == "__main__":
    main()