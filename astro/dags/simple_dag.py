from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago


with DAG(dag_id="simple_dag",
         schedule_interval="@daily",
         start_date=days_ago(3),
         catchup=False) as dag:
    task_1 = DummyOperator(task_id="task_1")