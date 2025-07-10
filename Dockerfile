# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if exists
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# run migrations
RUN python manage.py migrate

# populate the database if needed
RUN python manage.py populate_sample_data


# Expose port (change if your app uses a different port)
EXPOSE 8000

# Default command 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
