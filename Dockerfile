# Base image
FROM python:3.10

# Set working directory
WORKDIR /mathbackend

# Copy files
COPY ./backend /mathbackend/backend

COPY ./requirements.txt /mathbackend/requirements.txt


# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8000
CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
