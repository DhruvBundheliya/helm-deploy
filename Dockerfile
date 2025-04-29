# -------------------------
# 🐳 Dockerfile
# -------------------------
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl bash gnupg && \
    curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash && \
    apt-get clean

WORKDIR /app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/main.py"]
