FROM python:3.8-alpine

COPY . /app
WORKDIR /app

EXPOSE 8000

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "python app.py"]