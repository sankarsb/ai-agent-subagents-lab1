FROM python:3.12-slim

WORKDIR /app

COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
