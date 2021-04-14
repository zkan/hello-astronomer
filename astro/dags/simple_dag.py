from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils import timezone


with DAG(dag_id="simple_dag",
         schedule_interval="*/10 * * * *",
         start_date=timezone.datetime(2021, 1,1 )) as dag:
    task_1 = DummyOperator(task_id="task_1")