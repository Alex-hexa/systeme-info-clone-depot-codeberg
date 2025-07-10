import datetime

from airflow.sdk import DAG, Asset
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.utils.trigger_rule import TriggerRule

with DAG(dag_id='6_audit', schedule=[Asset('file://myfile.txt')]):
    # créer une table audit
    t_create = SQLExecuteQueryOperator(task_id='t_create', conn_id='db_result',
    sql="""
        CREATE TABLE result_audit (
            id SERIAL PRIMARY KEY,
            elapsed_time INTERVAL
        );
    """)
    t_update_audit = SQLExecuteQueryOperator(task_id='t_update_audit', conn_id='db_result',
    sql="""
        INSERT INTO result_audit (elapsed_time)
        VALUES ((SELECT MAX(recorded) - MIN(recorded) FROM result_img));
    """, trigger_rule=TriggerRule.ALL_DONE)
    t_create >> t_update_audit
    # insérer des données dans la table audit