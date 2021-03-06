from datetime import timedelta

from airflow import DAG
from airflow.models.baseoperator import chain, cross_downstream
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago


def _downloading_data(my_param, ds, ti, **kwargs):
    print("Just a test")
    print(my_param)
    print(ds)
    print(kwargs)

    with open("/tmp/my_file.txt", "w") as f:
        f.write("my_data")

    ti.xcom_push(key="my_key", value=43)

    return 42


def _checking_data(ti):
    print("Checking data")
    my_xcom = ti.xcom_pull(key="return_value", task_ids=["downloading_data"])
    print(my_xcom)
    my_key = ti.xcom_pull(key="my_key", task_ids=["downloading_data"])
    print(my_key)


def _failure(context):
    print("On callback failure")
    print(context)


default_args = {
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email_on_retry": True,
    "email": ["kan@odds.team"]
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

    checking_data = PythonOperator(
        task_id="checking_data",
        python_callable=_checking_data,
    )

    waiting_for_data = FileSensor(
        task_id="waiting_for_data",
        fs_conn_id="fs_default",
        filepath="my_file.txt",
        poke_interval=5,
    )

    processing_data = BashOperator(
        task_id="processing_data",
        bash_command="exit 0",
        on_failure_callback=_failure,
    )

    downloading_data >> [checking_data, waiting_for_data] >> processing_data
    # chain(downloading_data, waiting_for_data, processing_data)
    # cross_downstream([downloading_data, checking_data], [waiting_for_data, processing_data])