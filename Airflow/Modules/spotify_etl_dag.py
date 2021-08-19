from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from Spotify_ETL_Modules.token_request import token_extraction

default_args = {
	"owner" : "airflow", 
	"depends_on_past" : False,
	"start_date" : datetime.now(), #year,month,day,hour,minutes,seconds
	"email" : ["airflow@example.com"],
	"email_on_failure" : False,
	"email_on_retry" : False, 
	"retries" : 1,
	"retry_delay" : timedelta(minutes = 1)
}

dag = DAG(
	'Spotify_Recently_Played_Tracks_ETL', 
	default_args=default_args,
	description="Spotify Recently Played Tracks",
	catchup=False,
	schedule_interval="0 0 * * * *"
)

spotify_etl_run = PythonOperator(
	task_id="spotify_project",
	python_callable=token_extraction,
	dag=dag
)

#spotify_etl_run = BashOperator(
#	task_id="spotify_project",
#	bash_command='/Users/ernesto/Desktop/spotify_etl.sh',
#	dag=dag
#)

spotify_etl_run