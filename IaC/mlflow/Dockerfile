FROM python:latest

RUN pip install -U pip & pip install mlflow
RUN pip install psycopg2 google-cloud-storage

COPY run_mlflow.sh .
RUN chmod u+x ./run_mlflow.sh
CMD ./run_mlflow.sh
