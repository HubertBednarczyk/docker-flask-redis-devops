FROM python:3.11-slim

WORKDIR /app

# najpierw biblioteki – dzięki temu cache się lepiej wykorzystuje
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# potem reszta kodu
COPY . .

CMD ["python", "app.py"]
