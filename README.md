# 🚀 Helm Upgrade Action

A GitHub Action to deploy Helm charts using Python. It wraps `helm upgrade --install` and exposes structured inputs for fine control of Helm flags.

## ✅ Features

- 🔄 Upgrade or install Helm releases
- 🧩 Full support for Helm CLI flags like `--set`, `--values`, `--version`, etc.
- 🐍 Implemented in Python for readability and flexibility
- 📦 Docker-based packaging with lint/build/test workflows

## 🔧 Usage

```yaml
- name: Deploy using Helm Upgrade Pro
  uses: DhruvBundheliya/helm-deploy@v1.0.0
  with:
    release: my-app
    chart: ./charts/my-app
    kubeconfig: ${{ secrets.KUBECONFIG }}
    namespace: production
    atomic: true
    wait: true
    timeout: 10m
    values: |
      replicaCount: 2
      image:
        tag: v1.2.3
```

### 📘 More Examples

**Minimal Deployment**
```yaml
- uses: DhruvBundheliya/helm-deploy@v1.0.0
  with:
    release: my-app
    chart: ./charts/app
    kubeconfig: ${{ secrets.KUBECONFIG }}
```

**Advanced Overrides**
```yaml
- uses: DhruvBundheliya/helm-deploy@v1.0.0
  with:
    release: web
    chart: ./charts/web
    kubeconfig: ${{ secrets.KUBECONFIG }}
    set: |
      image.tag=latest
      service.type=LoadBalancer
    atomic: true
    reuse_values: true
```

## 📥 Inputs

| Name               | Description                                  | Default   | Required |
|--------------------|----------------------------------------------|-----------|----------|
| release            | Helm release name                            | —         | ✅        |
| chart              | Chart path or reference                      | —         | ✅        |
| kubeconfig         | Base64-encoded kubeconfig                    | —         | ✅        |
| namespace          | Kubernetes namespace                         | `default` | ❌        |
| create_namespace   | Create Kubernetes namespace if not available | `false`   | ❌        |
| version            | Chart version constraint                     | —         | ❌        |
| values             | Inline YAML values (multiline)               | —         | ❌        |
| set                | `--set` values                               | —         | ❌        |
| set_string         | `--set-string` values                        | —         | ❌        |
| set_file           | `--set-file` paths                           | —         | ❌        |
| timeout            | Operation timeout                            | `5m0s`    | ❌        |
| atomic             | Rollback on failure                          | `false`   | ❌        |
| wait               | Wait until resources are ready               | `false`   | ❌        |
| dry_run            | Simulate install                             | `false`   | ❌        |
| install            | Enable install if not already present        | `true`    | ❌        |
| reuse_values       | Merge with previous values                   | `false`   | ❌        |
| reset_values       | Reset to chart defaults                      | `false`   | ❌        |
| cleanup_on_fail    | Delete resources on failure                  | `false`   | ❌        |
| dependency_update  | Update missing chart deps                    | `true`    | ❌        |
| post_renderer      | Path to post-renderer binary                 | —         | ❌        |
| post_renderer_args | Extra arguments for post-renderer            | —         | ❌        |

## 📝 License

[MIT](./LICENSE)

---
Made by Dhruv bundheliya
