#  Cricket Statistics Pipeline with Google Cloud Services
 From retrieving data via the Cricbuzz API to crafting a dynamic Looker Studio dashboard, each phase contributes to the seamless flow of data for analysis and visualization.

### Architecture

![Architecture](https://github.com/PanniePB/data-engineering-project/blob/main/Architecture.png)


### Data Retrieval with Python and Cricbuzz API
The foundation of my project begins with Python’s prowess in interfacing with APIs. The methods of fetching cricket statistics from the Cricbuzz API, harnessing the power of Python to gather the required data efficiently.

### Storing Data in Google Cloud Storage (GCS)
Once the data is obtained,  next step involves preserving it securely in the cloud. Explore how to store this data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing.

### Creating a Cloud Function Trigger
With  data safely stored, we proceed to set up a Cloud Function that acts as the catalyst for  pipeline. This function triggers upon file upload to the GCS bucket, serving as the initiator for  subsequent data processing steps.


### Execution of the Cloud Function 06-07-2024
Within the Cloud Function, intricate code is crafted to precisely trigger a Dataflow job. We’ll meticulously handle triggers and pass the requisite parameters to seamlessly initiate the Dataflow job, ensuring a smooth flow of data processing.

### Dataflow Job for BigQuery 06-07-2024
The core of  pipeline lies in the Dataflow job. Triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery. We’ll meticulously configure the job settings to ensure optimal performance and accurate data ingestion into BigQuery.

### Looker Dashboard Creation 06-07-2024
Created a visually compelling dashboard. This dashboard will serve as the visualization hub, enabling insightful analysis based on the data loaded from  cricket statistics pipeline.
![Looker](https://github.com/PanniePB/data-engineering-project/blob/main/Looker.png)

## Future Goals 
Explore more services provided by GOOGLE Cloud Platform primarily FinOps framework.
