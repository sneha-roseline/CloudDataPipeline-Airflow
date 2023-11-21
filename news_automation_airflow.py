import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from newsapi_fetch import runner
from airflow.providers.amazon.aws.hooks.base_aws import AwsGenericHook
import time
from airflow.providers.amazon.aws.sensors.glue import GlueJobSensor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the 'args' variable with appropriate configuration settings
args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'email': ['myemail@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15),
}

dag = DAG(
    dag_id="news_automation_dag",
    default_args=args,
    schedule_interval=None
)

def glue_job_s3_dests3_transfer(job_name, **kwargs):
    session = AwsGenericHook(aws_conn_id='aws_s3_conn')

    # Get a client in the same region as the Glue job
    boto3_session = session.get_session(region_name='us-east-2')

    # Trigger the job using its name
    client = boto3_session.client('glue')
    client.start_job_run(
        JobName=job_name,
    )

def get_run_id():
    time.sleep(8)
    session = AwsGenericHook(aws_conn_id='aws_s3_conn')
    boto3_session = session.get_session(region_name='us-east-2')
    glue_client = boto3_session.client('glue')
    response = glue_client.get_job_runs(JobName="newsapi-etl-job")
    job_run_id = response["JobRuns"][0]["Id"]
    return job_run_id

with dag:

    extract_news_info = PythonOperator(
        task_id='extract_news_info',
        python_callable=runner,
        dag=dag,
    )

    move_file_to_s3 = BashOperator(
        task_id="move_file_to_s3",
        bash_command='aws s3 mv {{ ti.xcom_pull("extract_news_info") }}  s3://landings3bucket-sneha',
    )

    glue_job_trigger = PythonOperator(
        task_id='tsk_glue_job_trigger',
        python_callable=glue_job_s3_dests3_transfer,
        op_kwargs={
            'job_name': 'newsapi-etl-job'
        },
    )

    grab_glue_job_run_id = PythonOperator(
        task_id='tsk_grab_glue_job_run_id',
        python_callable=get_run_id,
    )

    is_glue_job_finish_running = GlueJobSensor(
        task_id="tsk_is_glue_job_finish_running",
        job_name='newsapi-etl-job',
        run_id='{{task_instance.xcom_pull("tsk_grab_glue_job_run_id")}}',
        verbose=True,  # prints glue job logs in airflow logs
        aws_conn_id='aws_s3_conn',
        poke_interval=60,
        timeout=3600,
    )

extract_news_info >> move_file_to_s3 >> glue_job_trigger >> grab_glue_job_run_id >> is_glue_job_finish_running
