from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import spotify_etl
from airflow.utils.dates import days_ago

default_args = {
	"owner": "airflow",
	"depends_on_past" : False,
	"start_date" : datetime(2021, 8, 16, 14, 00, 00), #year,month,day,hour,minutes,seconds
	"email" : ["airflow@example.com"],
	"email_on_failure" : False,
	"email_on_retry" : False, 
	"retries" : 1,
	"retry_delay" : timedelta(minutes = 1)
}

dag = DAG(
	'Spotify_ETL', 
	default_args=default_args,
	description="Spotify ETl",
	catchup=False,
	schedule_interval="0 0 * * *"
)

spotify_etl_run = PythonOperator(
	task_id="spotify_project",
	python_callable=spotify_etl,
	dag=dag
)

spotify_etl_run