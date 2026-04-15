FROM python:3.11

WORKDIR /app

COPY services/api /app
COPY models /app/models

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]