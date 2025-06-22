# Dockerfile

FROM python:3.10-slim

# System packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 🔧 Install sentencepiece manually (this fixes Pegasus error)
RUN pip install sentencepiece

# Set the entry point
CMD ["python", "main.py"]
