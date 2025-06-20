* https://dbml.dbdiagram.io/docs/
* https://astronomer.github.io/astronomer-cosmos/
* https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
* https://medium.com/@luisfelipe_342/orchestrating-multiple-dbt-projects-using-a-single-airflow-instance-on-kubernetes-0b1d270c07f9

airflow-scheduler - The scheduler monitors all tasks and dags, then triggers the task instances once their dependencies are complete.
airflow-dag-processor - The DAG processor parses DAG files.
airflow-api-server - The api server is available at http://localhost:8080.
airflow-worker - The worker that executes the tasks given by the scheduler.
airflow-triggerer - The triggerer runs an event loop for deferrable tasks.
airflow-init - The initialization service.
postgres - The database.
redis - The redis - broker that forwards messages from scheduler to worker.
