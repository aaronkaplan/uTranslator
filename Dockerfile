# Use the official Python 3.12 Alpine base image for a lightweight setup
FROM python:3.12-alpine

# Prevent Python from writing pyc files and ensure output is sent straight to terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary system dependencies
RUN apk update && apk add --no-cache build-base libffi-dev curl

# Create a non-root user for better security
RUN adduser -D appuser

# Set the working directory to /app
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire application code to the working directory
COPY . .

# Change ownership of the application directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose port 8000 to allow communication with the server
EXPOSE 9948

# Define the healthcheck to monitor the /healthcheck endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:9948/healthcheck || exit 1

# Define the default command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9948"]

