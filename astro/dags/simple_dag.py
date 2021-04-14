from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def _downloading_data(**kwargs):
    print("Just a test")
    print(kwargs)


default_args = {
    "retry": 5,
    "retry_delay": timedelta(minutes=5)
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

    downloading_data = PythonOperator(
        task_id="downloading_data",
        python_callable=_downloading_data,
    )