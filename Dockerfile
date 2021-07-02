FROM python:3.8-buster

WORKDIR /app
COPY . /app

RUN make install-requirements

ENTRYPOINT ["python", "/app/autoforecast/automl.py"]