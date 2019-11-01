FROM python:alpine

WORKDIR /app
COPY api.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
