import boto3

GLUE_JOB_NAME = "process_reviews_job"

def lambda_handler(event, context):
    glue_client = boto3.client('glue')

    print("Received event:", event)

    try:
        print(f"Starting AWS Glue job: {GLUE_JOB_NAME}")
        response = glue_client.start_job_run(JobName=GLUE_JOB_NAME)
        print(f"Job started successfully. Run ID: {response['JobRunId']}")

        return {
            'statusCode': 200,
            'body': 'Glue job started'
        }

    except Exception as e:
        print(f"Error: {e}")
        raise e