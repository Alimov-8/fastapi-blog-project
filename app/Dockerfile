# Pull base image
FROM python:3.9

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy project
COPY . /code/

# Run with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]