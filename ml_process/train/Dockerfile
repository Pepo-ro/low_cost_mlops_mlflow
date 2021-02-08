FROM google/cloud-sdk:slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip
RUN pip3 install -r requirements.txt 

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app