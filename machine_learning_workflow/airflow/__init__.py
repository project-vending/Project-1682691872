 python
import os

# Define path to airflow directory
AIRFLOW_DIR = 'machine_learning_workflow/airflow'

# Check if directory exists, if not create it
if not os.path.exists(AIRFLOW_DIR):
    os.makedirs(AIRFLOW_DIR)

# Create empty __init__.py file
open(os.path.join(AIRFLOW_DIR, '__init__.py'), 'a').close()
