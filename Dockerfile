# -------------------------
# 🐳 Dockerfile
# -------------------------
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl bash gnupg && \
    curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash && \
    apt-get clean

WORKDIR /github/workspace
COPY main.py /github/workspace/main.py
COPY requirements.txt /github/workspace/requirements.txt
RUN pip install -r /github/workspace/requirements.txt

ENTRYPOINT ["python", "/github/workspace/main.py"]