"""Simple DAG to run only the seeds models in dbt using Cosmos."""

from datetime import datetime

from cosmos import DbtDag, ProjectConfig, RenderConfig
from include.constants import (
    retail_analytics_path,
    venv_execution_config,
)
from include.profiles import airflow_db

only_seeds = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path=retail_analytics_path,
        # manifest_path=manifest_path,
    ),
    profile_config=airflow_db,
    execution_config=venv_execution_config,
    # new render config
    render_config=RenderConfig(
        select=["path:seeds"],
    ),
    # normal dag parameters
    schedule="@monthly",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    doc_md=__doc__,
    default_args={"retries": 2},
    dag_id="seed_only_dag",
    tags=["filtering"],
)
