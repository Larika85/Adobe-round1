# Use an official Python image, for linux/amd64
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory inside container
WORKDIR /app

# Copy code into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make sure input/output directories exist
RUN mkdir -p input output

# Define the command to run all PDFs inside /app/input
CMD ["python", "-u", "batch_run.py"]
