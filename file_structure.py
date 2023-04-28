
import os

# Define project root directory
PROJECT_ROOT = 'machine_learning_workflow'

# Define subdirectories
AIRFLOW_DIR = os.path.join(PROJECT_ROOT, 'airflow')
SAGEMAKER_DIR = os.path.join(PROJECT_ROOT, 'sagemaker')
STREAMLIT_DIR = os.path.join(PROJECT_ROOT, 'streamlit')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

# Define file names
TRAINING_SCRIPT_FILE = 'train.py'
DEPLOYMENT_SCRIPT_FILE = 'deploy.py'

# Create directories
os.makedirs(AIRFLOW_DIR, exist_ok=True)
os.makedirs(SAGEMAKER_DIR, exist_ok=True)
os.makedirs(STREAMLIT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Create empty files
for directory in [AIRFLOW_DIR, SAGEMAKER_DIR, STREAMLIT_DIR, DATA_DIR]:
    with open(os.path.join(directory, '__init__.py'), 'w'):
        pass

with open(os.path.join(SAGEMAKER_DIR, TRAINING_SCRIPT_FILE), 'w'):
    pass

with open(os.path.join(SAGEMAKER_DIR, DEPLOYMENT_SCRIPT_FILE), 'w'):
    pass
