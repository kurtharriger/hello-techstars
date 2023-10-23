# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask mode 
ARG FLASK_ENV=production
ENV FLASK_ENV=${FLASK_ENV}

# Conditionally use Gunicorn or Flask's built-in server
CMD if [ "$FLASK_ENV" = "production" ]; then \
        exec gunicorn -b 0.0.0.0:5001 app:app; \
    else \
        exec python app.py; \
    fi
