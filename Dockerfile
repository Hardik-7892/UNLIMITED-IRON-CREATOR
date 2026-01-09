# Use Python 3.10 slim base image for optimal size
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
# Note: streamlit, pandas, and numpy are explicitly installed
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir streamlit>=1.28.0 pandas>=2.0.0 numpy>=1.24.0

# Copy application files
COPY . .

# Create output directory for generated media
RUN mkdir -p generated_media

# Expose port 8080 (Cloud Run standard)
EXPOSE 8080

# Health check (optional but recommended)
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health || exit 1

# Run Streamlit with Cloud Run configuration
CMD streamlit run streamlit_app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false
