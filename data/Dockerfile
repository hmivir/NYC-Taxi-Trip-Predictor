FROM python:3.8.16-slim

WORKDIR /app

# Install minimal requirements for data download
COPY requirements_data.txt .
RUN pip install --no-cache-dir -r requirements_data.txt

# Copy only the data download script
COPY . .

# Create data directories
RUN mkdir -p /app/data/raw /app/data/processed

# Set entrypoint to the download script
ENTRYPOINT ["python", "/app/data/download_data.py"] 