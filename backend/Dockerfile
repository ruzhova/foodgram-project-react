FROM python:3.7-slim

WORKDIR /backend

COPY foodgram/requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY foodgram/ .

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]