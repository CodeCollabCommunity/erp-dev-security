FROM python:3.12.2-slim

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN apt-get update \
    && apt-get clean \
    && apt-get -y install openssh-client libpq-dev curl nano

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV TZ="America/Mexico_City"
ENV NAME .env

RUN pwd

COPY  . .

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "55"]
