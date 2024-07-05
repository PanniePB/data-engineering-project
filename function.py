from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "data-engineering-project"

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


    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

