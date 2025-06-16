"""A simple DAG that uses Cosmos to render a dbt project as a TaskGroup."""

from datetime import datetime

from cosmos import DbtTaskGroup, ProjectConfig
from include.constants import (
    manifest_path,
    retail_analytics_path,
    venv_execution_config,
)
from include.profiles import airflow_db

from airflow.operators.empty import EmptyOperator
from airflow.sdk import DAG

with DAG(
    schedule="@hourly",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
    dag_id="simple_task_group_dag",
    doc_md=__doc__,
    default_args={"retries": 2},
) as simple_task_group_dag:
    """
    A simple DAG that uses Cosmos to render a dbt project as a TaskGroup.
    """

    pre_dbt = EmptyOperator(task_id="pre_dbt")

    jaffle_shop = DbtTaskGroup(
        group_id="retail_analytics_project",
        project_config=ProjectConfig(
            dbt_project_path=retail_analytics_path,
            manifest_path=manifest_path,
        ),
        profile_config=airflow_db,
        execution_config=venv_execution_config,
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> jaffle_shop >> post_dbt
