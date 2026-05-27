FROM python:3.11-slim

# Prevents python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Shows logs directly in terminal
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Flask runs on port 5000
EXPOSE 5000

CMD ["python", "app.py"]