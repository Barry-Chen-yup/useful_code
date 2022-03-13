#!/bin/sh
export AIRFLOW_HOME=/workspace/airflow
echo "export AIRFLOW_HOME=/workspace/airflow" >> ~/.bashrc
airflow db init
airflow users create \
--username admin \
--firstname barry \
--lastname chen \
--password airflow \
--role Admin \
--email akj00173@gmail.com
airflow webserver --port 8080 -D
airflow scheduler -D