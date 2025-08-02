FROM python:3.10-slim

# Install system dependencies
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg git neofetch apt-utils libmediainfo0v5 sqlite3 \
    libgl1-mesa-glx libglib2.0-0 libxml2-dev libxslt-dev sudo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

# Copy entire app source
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Make start script executable (optional but safe)
RUN chmod +x start

# Set entrypoint to use bash to run the script named "start"
ENTRYPOINT ["bash", "start"]
