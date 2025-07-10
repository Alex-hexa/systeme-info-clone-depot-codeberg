from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(dag_id='empty_dag'):
    extract = EmptyOperator(task_id='extract')
    transform = EmptyOperator(task_id='transform')
    load = EmptyOperator(task_id='load')
    extract >> transform >> load
