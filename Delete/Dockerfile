FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MEMORY_PATH=/data/brain.fs

VOLUME ["/data"]

CMD ["python", "main.py"]