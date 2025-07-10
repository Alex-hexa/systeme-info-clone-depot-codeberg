import datetime

from airflow.sdk import DAG, Asset
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(dag_id='5_pg',
        start_date=datetime.datetime(2025,7,6),
        is_paused_upon_creation=False,
        schedule=[Asset("s3://asset-bucket/example.csv")]
        ):
    create_result_img = SQLExecuteQueryOperator(
        task_id='create_result_img',
        conn_id='db_result',
        sql="""
            CREATE TABLE result_img (
                "id" SERIAL PRIMARY KEY,
                "nb_results" INT NOT NULL,
                "recorded" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                );""",
    )