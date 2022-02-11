# Pull base image
FROM python:3.9

ENV PYTHONBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy project
COPY . /app/

EXPOSE 8000

# Run with uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]