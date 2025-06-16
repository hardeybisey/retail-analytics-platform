"""Simple DAG to run dbt using Cosmos."""

from datetime import datetime

from cosmos import DbtDag, ProjectConfig
from include.constants import (
    manifest_path,
    retail_analytics_path,
    venv_execution_config,
)
from include.profiles import airflow_db

simple_dag = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(
        dbt_project_path=retail_analytics_path,
        manifest_path=manifest_path,
    ),
    profile_config=airflow_db,
    execution_config=venv_execution_config,
    # normal dag parameters
    doc_md=__doc__,
    default_args={"retries": 2},
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    dag_id="simple_dbt_dag",
    tags=["simple"],
)
