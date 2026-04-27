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
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Environment variables will be injected at runtime (from Codespaces or AWS)
CMD ["python", "src/app.py"]