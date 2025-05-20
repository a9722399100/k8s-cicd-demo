FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python", "app.py"]
