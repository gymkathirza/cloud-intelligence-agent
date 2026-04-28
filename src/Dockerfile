# Stage 1: Terraform Installer
FROM hashicorp/terraform:latest as terraform_bin

# Stage 2: Python Environment
FROM python:3.11-slim

# Copy Terraform binary from the first stage
COPY --from=terraform_bin /bin/terraform /usr/local/bin/terraform

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python requirements
COPY src/requirements.txt .
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY src .

EXPOSE 8501

# Environment variables will be injected at runtime (from Codespaces or AWS)
CMD ["streamlit", "run", "ui.py", "--server.port=8501", "--server.address=0.0.0.0"]