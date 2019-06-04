FROM python:3.7.3
COPY ./ /app
WORKDIR /app
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y sqlite3 libsqlite3-dev && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt 
RUN sqlite3 /app/storage.db
RUN sqlite3 /app/storage.db init_tables.sql
ENTRYPOINT ["python3"]
CMD ["app.py"]
