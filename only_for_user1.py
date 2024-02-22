from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "user1",
    "email_on_failure": "user1@example.com",
    "email_on_retry": "user1@example.com",
    "email": "user1@example.com",
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}

def _test():
    print("hi user1!")

with DAG(dag_id="only_for_user1",
    start_date=datetime(2022, 6, 25),
    schedule_interval="* * * * *",
    default_args=default_args,
    catchup=False,
    access_control={'user1':{'can_read', 'can_edit'}}
    ) as dag:

    test = PythonOperator(
        task_id="test",
        python_callable=_test,
    )
