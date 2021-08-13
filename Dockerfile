FROM cdaf/fastapi

COPY . /app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "python app.py"]