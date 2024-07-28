FROM bitnami/spark:3.5

# Set the working directory
WORKDIR /app

# Copy your application code
COPY ./app /app

# Install your Python dependencies (if any)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



# Run your application
CMD ["python3", "run.py"]