FROM python:3.5.2

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3000

CMD ["python", "app.py"]
