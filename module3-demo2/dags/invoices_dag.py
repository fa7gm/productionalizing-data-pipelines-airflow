from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.hooks.base_hook import BaseHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 11, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


with DAG(dag_id="invoices_dag",
         schedule_interval="@daily",
         default_args=default_args,
         catchup=False) as dag:

	download_invoices_instance = PythonOperator(
		task_id="download_invoices",
		python_callable=download_invoices_function
	)
