python
import boto3

# Define AWS credentials, region, and SageMaker endpoint name
AWS_ACCESS_KEY_ID = 'your_access_key_id_here'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key_here'
AWS_REGION_NAME = 'us-west-2'  # or your preferred region
SAGEMAKER_ENDPOINT_NAME = 'your_endpoint_name_here'

# Define function for deploying a trained model with the specified endpoint configuration
def deploy_model(model_data_path, model_name, endpoint_config_name):
    # Create SageMaker client object
    sagemaker_client = boto3.client('sagemaker', region_name=AWS_REGION_NAME,
                                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # Create SageMaker model object
    model_response = sagemaker_client.create_model(
        ModelName=model_name,
        PrimaryContainer={
            'Image': 'your_docker_image_here',
            'ModelDataUrl': model_data_path
        },
        ExecutionRoleArn='arn:aws:iam::your_iam_role_arn_here'
    )

    # Create SageMaker endpoint configuration object
    endpoint_config_response = sagemaker_client.create_endpoint_config(
        EndpointConfigName=endpoint_config_name,
        ProductionVariants=[
            {
                'VariantName': 'default',
                'ModelName': model_name,
                'InitialInstanceCount': 1,
                'InstanceType': 'ml.t2.medium'
            }
        ]
    )

    # Update SageMaker endpoint with the new configuration
    sagemaker_client.update_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT_NAME,
        EndpointConfigName=endpoint_config_name
    )

    return model_response, endpoint_config_response
