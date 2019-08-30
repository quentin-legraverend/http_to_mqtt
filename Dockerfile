FROM python:alpine

WORKDIR /app
COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
