"""
An example DAG that uses Cosmos to render a dbt project into an Airflow DAG.
"""

import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProfileConfig, ProjectConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

DEFAULT_DBT_ROOT_PATH = Path(__file__).parent / "dbt/retail_analytics"
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH))
MANIFEST_PATH = DBT_ROOT_PATH / "target/manifest.json"


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_dbt_conn",
        profile_args={
            "schema": "public",
            "host": "postgres_dbt",
            "user": "dbt",
            "password": "dbt",
            "port": 5432,
            "dbname": "retail_analytics",
        },
    ),
)

basic_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path=DBT_ROOT_PATH,
        manifest_path=MANIFEST_PATH,
        seeds_relative_path="seeds",
    ),
    profile_config=profile_config,
    operator_args={
        "install_deps": True,
        "full_refresh": True,
    },
    schedule="@daily",
    start_date=datetime(2025, 1, 2),
    catchup=False,
    dag_id="basic_cosmos_dag",
    default_args={"retries": 2},
)
