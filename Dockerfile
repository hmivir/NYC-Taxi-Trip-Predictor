FROM python:3.8.16-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN HDF5_DIR=/usr/lib/aarch64-linux-gnu/hdf5/serial/ \
    pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Create non-root user
RUN useradd -m jupyter
RUN chown -R jupyter:jupyter /app
USER jupyter

# Expose port for Jupyter
EXPOSE 8888

# Start Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"] 