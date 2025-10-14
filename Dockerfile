# Gunakan base image Python
FROM python:3.10-slim

# Tentukan working directory di dalam container
WORKDIR /app

# Copy semua file proyek ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask numpy pandas matplotlib scikit-learn

# Set environment variable untuk Flask
ENV FLASK_APP=visualization_flask/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Buka port Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["flask", "run"]
