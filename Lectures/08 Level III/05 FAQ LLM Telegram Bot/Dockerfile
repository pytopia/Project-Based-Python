# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY .env .
COPY src/ ./src/

# Add the current directory to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Set the command to run your bot
CMD ["python", "src/app.py"]
