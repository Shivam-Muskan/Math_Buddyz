# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY main.py /app
COPY requirements.txt /app
COPY backend /app/backend

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]