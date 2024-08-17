FROM python:3.10-slim-buster

WORKDIR /app

COPY src ./src
COPY internal ./internal

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]