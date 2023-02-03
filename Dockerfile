# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY backend /app

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8080
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]