import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

def python_read_file():
    with open('/opt/airflow/dags/data/access.log.1', 'r') as f:
        return f.readlines()


with DAG(dag_id='d_read_file',
            start_date=datetime.datetime(2025,6,30),
            schedule="*/5 * * * *",
            is_paused_upon_creation=True,
            catchup=False
            ):
    t_start = EmptyOperator(task_id='t_start')
    read_file_b = BashOperator(task_id='t_read_file_bash', bash_command='cat /opt/airflow/dags/data/access.log.1')
    read_file_p = PythonOperator(task_id='t_read_file_python', python_callable=python_read_file)
    t_start >> [read_file_b, read_file_p]
