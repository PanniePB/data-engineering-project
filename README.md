#  Cricket Statistics Pipeline with Google Cloud Services
 From retrieving data via the Cricbuzz API to crafting a dynamic Looker Studio dashboard, each phase contributes to the seamless flow of data for analysis and visualization.

### Architecture

![Architecture](https://github.com/vishal-bulbule/cricket-stat-data-engineering-project/blob/master/Architecture.png)

### Data Retrieval with Python and Cricbuzz API
The foundation of my project begins with Python’s prowess in interfacing with APIs. The methods of fetching cricket statistics from the Cricbuzz API, harnessing the power of Python to gather the required data efficiently.

### Storing Data in Google Cloud Storage (GCS)
Once the data is obtained,  next step involves preserving it securely in the cloud. Explore how to store this data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing.

### Creating a Cloud Function Trigger
With  data safely stored, we proceed to set up a Cloud Function that acts as the catalyst for  pipeline. This function triggers upon file upload to the GCS bucket, serving as the initiator for  subsequent data processing steps.

## Future goals

### Execution of the Cloud Function
### Dataflow Job for BigQuery
### Looker Dashboard Creation

