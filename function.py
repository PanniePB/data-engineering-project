from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import logging

def trigger_df_job(cloud_event, context):
    try:
        # Set up the Dataflow service
        service = build('dataflow', 'v1b3')
        project = "data-engineering-project"

        # Define the template path and job parameters
        template_path = "gs://dataflow-templates-australia-southeast1/latest/GCS_Text_to_BigQuery"

        template_body = {
            "jobName": "bq-load1",
            "parameters": {
                "javascriptTextTransformGcsPath": "gs://bucket-dataflow-metadata1/udf.js",
                "JSONPath": "gs://bucket-dataflow-metadata1/bq.json",
                "javascriptTextTransformFunctionName": "transform",
                "outputTable": "concrete-plasma-428403-g9.cricket_dataset.icc_odi_batsman_ranking",
                "inputFilePattern": "gs://bucket-ranking-data-1/batsmen_rankings.csv",
                "bigQueryLoadingTemporaryDirectory": "gs://bucket-dataflow-metadata1",
            }
        }

        # Launch the Dataflow template
        request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
        response = request.execute()
        logging.info("Dataflow job launched successfully: %s", response)
        print(response)

    except HttpError as err:
        logging.error("HttpError occurred: %s", err)
        print(f"HttpError occurred: {err}")
    except Exception as e:
        logging.error("An error occurred: %s", e)
        print(f"An error occurred: {e}")

# Example usage
trigger_df_job(cloud_event=None, context=None)
