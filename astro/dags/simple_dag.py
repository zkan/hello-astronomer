from datetime import timedelta

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago


def _downloading_data(my_param, ds, **kwargs):
    print("Just a test")
    print(my_param)
    print(ds)
    print(kwargs)

    with open("/tmp/my_file.txt", "w") as f:
        f.write("my_data")


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
        op_kwargs={"my_param": 42},
    )

    waiting_for_data = FileSensor(
        task_id="waiting_for_data",
        fs_conn_id="fs_default",
        filepath="my_data.txt",
        poke_interval=5,
    )

    processing_data = BashOperator(
        task_id="processing_data",
        bash_command="exit 0",
    )

    # downloading_data >> waiting_for_data >> processing_data
    chain(downloading_data, waiting_for_data, processing_data)