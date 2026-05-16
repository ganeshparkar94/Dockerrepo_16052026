# Use lightweight Python image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application file
COPY app.py .

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
