FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn python-dotenv

COPY . .

CMD ["gunicorn", "--config", "gunicorn.py", "app:app"]