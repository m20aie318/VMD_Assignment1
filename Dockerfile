# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask directly
RUN pip install Flask

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Define the command to run your Flask app
CMD ["python", "server.py"]
