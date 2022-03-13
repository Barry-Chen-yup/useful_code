from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
import os, airflow
from airflow.utils.dates import days_ago
from airflow.operators.email import EmailOperator
import pendulum
import time

local_tz = pendulum.timezone("Asia/Taipei")

def fun():
    
    os.system('pwd')
    print('start calculate')
    # a=np.array([[1],[2]])
    # print(a)
    start_time=time.time()
    cmd = "python3 /workspace/tracker/code/track_chicken_test.py '/workspace/nas-data/Animal/chicken_video/'$(date -d 'yesterday' +%Y%m%d)"
    #os.setuid(0)
    ret = os.system(cmd)
    print('return number',ret)
    end_time=time.time()
    print('Total time',(end_time-start_time))
default_args = {
    'owner': 'someone',
    'depends_on_past': False,
    #'start_date': airflow.utils.dates.days_ago(1),
    'email': ['akj00173@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
    dag_id='test_print',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    catchup=False, # missing a dag not run again
    tags=['example'],
    max_active_runs=1, # Follow a sequence to avoid deadlock when using MySQL
) as dag:

    # python_timestamp = PythonOperator(
    #     task_id='python',
    #     python_callable=fun,
    #     #provide_context=True,
    #     #dag=dag
    # )        
    cleanup_task = BashOperator(
        task_id='task_1_data_file_cleanup',
        # cmd = 'python3 /workspace/tracker/code/track_chicken_test.py "/workspace/nas-data/Animal/chicken_video/"$(date -d "yesterday" +%Y%m%d)'
        bash_command='python3 /workspace/tracker/code/track_chicken_date_gpu.py "/workspace/nas-data/Animal/chicken_video/"$(date -d "yesterday" +%Y%m%d)',
        dag=dag
    )
    email_task = EmailOperator(
        task_id='send_email',
        to='akj00173@gmail.com',
        subject='Airflow success',
        html_content=""" <h3>Email Test</h3> {{ execution_date }}<br/>""",
        dag=dag
    )
    cleanup_task >> email_task
