import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id='enabled_default',
            start_date=datetime.datetime(2025,6,10),
            schedule="*/2 * * * *",
            is_paused_upon_creation=False,
            catchup=False
            ):
    t1 = BashOperator(task_id='t1', bash_command='date')
