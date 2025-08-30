# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy the backend service folder into the container
COPY trueproof-service/ /app

# Copy root requirements.txt (or use the one in service if different)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Start FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
