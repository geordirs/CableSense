# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directories for data and logs
RUN mkdir -p data models logs

# Expose the API port
EXPOSE 5000

# Set environment variables
ENV PYTHONPATH=/app

# Start the API server by default
CMD ["python", "src/api.py"]
