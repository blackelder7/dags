from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "user2",
    "email_on_failure": "user2@example.com",
    "email_on_retry": "user2@example.com",
    "email": "user2@example.com",
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}

with DAG(dag_id="only_for_user2",
    start_date=datetime(2022, 6, 25),
    schedule_interval="* * * * *",
    default_args=default_args,
    catchup=False,
    access_control={'user2':{'can_read', 'can_edit'}}
    ) as dag:

    test = BashOperator(
            task_id='test',
            bash_command='echo "hello user2!"',
    )
