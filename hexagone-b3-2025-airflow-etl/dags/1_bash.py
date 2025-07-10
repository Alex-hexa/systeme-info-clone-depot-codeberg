from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id='bash_dag'):
    t1 = BashOperator(task_id='t1', bash_command='echo "hello"')
