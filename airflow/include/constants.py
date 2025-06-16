"Contains constants used in the DAGs"

from pathlib import Path

from cosmos import ExecutionConfig

retail_analytics_path = Path("/usr/local/airflow/dbt/retail_analytics")
dbt_executable = Path("/usr/local/airflow/dbt_venv/bin/dbt")
manifest_path = Path("/usr/local/airflow/dbt/retail_analytics/target/manifest.json")
venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable),
)
