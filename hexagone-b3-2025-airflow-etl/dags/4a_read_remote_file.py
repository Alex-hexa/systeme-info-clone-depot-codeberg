import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.http.operators.http import HttpOperator

import os

def check_file_deleted():
    file_name = '/tmp/access.log.1'
    if os.path.exists(file_name):
        raise FileExistsError(file_name)


with DAG(
    dag_id='4a_read_remote_file',
    start_date=datetime.datetime(2025,6,30),
    schedule="*/10 * * * *",
    catchup=False,
    is_paused_upon_creation=False):
    t_curl = BashOperator(task_id='t_curl', bash_command="curl http://daa28417-5235-405c-a3b6-00e5333d7dc7.pub.instances.scw.cloud:8081/access.log.1 -o /tmp/access.log.1 && cat /tmp/access.log.1")
    t_count = BashOperator(task_id='t_count', bash_command="grep -c image.png /tmp/access.log.1 > /tmp/result.txt")
    t_delete = BashOperator(task_id='t_delete', bash_command="rm /tmp/access.log.1")
    t_check = PythonOperator(task_id='t_check_delete', python_callable=check_file_deleted)
    t_curl >> t_count >> t_delete >> t_check
