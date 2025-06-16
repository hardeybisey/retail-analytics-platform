"""Sample DAG demonstrating the use of Airflow SDK with BashOperator and task decorator."""

from datetime import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, task

with DAG(
    dag_id="demo",
    start_date=datetime(2025, 1, 1),
    schedule="0 0 * * *",
    tags=["demo"],
    doc_md=__doc__,
    default_args={"retries": 2},
) as dag:
    start = BashOperator(task_id="start", bash_command="echo 'start airflow'")
    end = BashOperator(task_id="end", bash_command="echo 'end airflow'")

    @task()
    def from_airflow():
        return "Airflow SDK!"

    @task()
    def say_hello_from(name: str):
        return f"Hello from {name}!"

    # pass xcom between tasks
    start >> say_hello_from(from_airflow()) >> end
