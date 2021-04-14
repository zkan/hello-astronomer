from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}
with DAG(dag_id="simple_dag",
         default_args=default_args,
         schedule_interval="@daily",
         start_date=days_ago(3),
         catchup=False) as dag:
    
    task_1 = DummyOperator(
        task_id="task_1",
    )

    task_2 = DummyOperator(
        task_id="task_2",
    )

    task_3 = DummyOperator(
        task_id="task_3",
    )