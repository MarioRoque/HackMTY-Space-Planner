FROM python:3.7.3

ENV PYTHONUNBUFFERED True

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py .
COPY Api ./Api

CMD ["python", "server.py"]