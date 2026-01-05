from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'hello_world',
    default_args={'owner': 'airflow'},
    description='A simple hello world DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    
    hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow!"',
    )
