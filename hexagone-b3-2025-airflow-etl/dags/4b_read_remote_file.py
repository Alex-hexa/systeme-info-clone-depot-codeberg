import datetime

from airflow.sdk import DAG, task, Asset
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

def my_filter(line):
    print(f'########## {line}')
    return 'image.png' in line

def count_image_png(task_instance):
    http_response = task_instance.xcom_pull(task_ids='t_http').split('\n')
    filter_result = filter(my_filter, http_response)
    list_result = list(filter_result)
    print(list_result)
    result = len(list_result)
    return result

def save_res(task_instance):
    nb_lines = task_instance.xcom_pull(task_ids='t_count')
    with open('/tmp/resultb.txt', 'w') as f:
        f.write(f'Nb rows: {nb_lines}')

@task(outlets=[Asset('file://myfile.txt')])
def save_res_db(task_instance):
    nb_lines = task_instance.xcom_pull(task_ids='t_count')
    query = f'INSERT INTO result_img(nb_results) VALUES ({nb_lines})'
    postgres_hook = PostgresHook(postgres_conn_id="db_result")
    conn = postgres_hook.get_conn()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()   


with DAG(
    dag_id='4b_read_remote_file',
    start_date=datetime.datetime(2025,6,30),
    schedule="*/10 * * * *",
    catchup=False,
    is_paused_upon_creation=False):
    t_curl = BashOperator(task_id='t_curl', bash_command="curl http://daa28417-5235-405c-a3b6-00e5333d7dc7.pub.instances.scw.cloud:8081/access.log.1 -o /tmp/access.log.1 && cat /tmp/access.log.1")
    t_http = HttpOperator(task_id='t_http', http_conn_id="httpfile", endpoint="access.log.1", method="GET", log_response=False)
    t_count = PythonOperator(task_id='t_count', python_callable=count_image_png, outlets=[Asset("s3://asset-bucket/example.csv")])
    t_save_res = PythonOperator(task_id='t_save_res', python_callable=save_res)
    # task : Compter le nombre de lignes contenant image.png
    # task : écrire le résultat dans un fichier dans /tmp/result.txt
    t_curl >> t_http >> t_count >> [t_save_res, save_res_db()]
