# Gunakan base image Python
FROM python:3.11-slim

# Tentukan working directory di dalam container
WORKDIR /app

# Copy semua file proyek ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Set environment variable untuk Flask
ENV FLASK_APP=visualization_flask/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Buka port Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["flask", "run"]

