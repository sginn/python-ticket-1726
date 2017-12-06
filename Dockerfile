FROM python:3.6-slim

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y gcc unixodbc-dev
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3000

CMD ["python3", "app.py"]
