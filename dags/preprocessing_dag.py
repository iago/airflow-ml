from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import os, sys
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

from make_dataset import make_dataset

DESTINATION_DIRECTORY = os.path.join(PARENT_DIR, 'data', 'processed')
DESTINATION_FILENAME = 'wine-dataset-{}'.format(
    datetime.strftime(datetime.now(), '%Y%m%d-%H%M%S'))

default_args = {
    'owner': 'Iago Nunes',
    'depends_on_past': False,
    'email': ['iago.nunes@grupoboticario.com.br'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    'ml_preprocessing',
    default_args=default_args,
    description='A DAG for Machine Learning preprocessing',
    schedule_interval=timedelta(minutes=30),
    start_date=datetime(2021, 11, 11),
    catchup=False,
    tags=['machine-learning']
)

prepare_data = PythonOperator(
    task_id='data_preparation',
    depends_on_past=False,
    python_callable=make_dataset,
    op_kwargs={
        'destination_directory': DESTINATION_DIRECTORY,
        'destination_filename': DESTINATION_FILENAME
    },
    dag=dag
)

prepare_data