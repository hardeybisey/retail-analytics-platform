"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

airflow_db = ProfileConfig(
    profile_name="retail_analytics",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="dbt_postgres",
        profile_args={"schema": "dbt"},
    ),
)
