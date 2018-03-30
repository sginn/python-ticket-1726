FROM python:3.6-slim

RUN apt-get update && apt-get install -y gcc unixodbc-dev

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install -e .

EXPOSE 3000

CMD ["gunicorn", "-c", "python:config.gunicorn", "app.app:create_app()"]