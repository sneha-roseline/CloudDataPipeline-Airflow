# Cloud ETL Pipeline with Airflow
 An ETL data pipeline with REST API, AWS, Spark, Airflow and much more!

 ## Description

 ### Objective
The project will fetch new related to a specific topic using News API by writing an ETL Python script and create a data pipeline that consumes the news data. 
The data coming in will be fetched based on a specific topic chosen to extract in our python script and extract the data in parquet format and directly stored on the AWS S3 landing bucket.
Built an ETL pipeline that would use AWS Glue to to load data from S3 landing bucket. In the ETL batch job, 
AWS glue involves using AWS glue crawler to crawl the data in S3 bucket to infer schemas and create a data catalogue. Transformations are applied and the results are store back to a destination s3 bucket.
Various AWS servcies like S3, EC2, AWS Glue, Data Catalogue, CloudWatch, AWS CLI along with IAMS were used. The entire process of fetching the data and the ETL pipeline was orchestrate using Apache Airflow which was run on AWS EC2 instance.

### Architecture
<img width="1343" alt="Screen Shot 2023-10-18 at 6 57 49 PM" src="https://github.com/sneha-roseline/CloudDataPipeline-Airflow/assets/146040464/21a4ccc3-9910-4022-9cf2-0e9aa64ee89c">

### Tools & Technologies

* Cloud - **[Amazon Web Sevices](https://aws.amazon.com/)**
* Batch Processing - **[Spark](https://spark.apache.org/)**
* Orchestration - **[Airflow](https://airflow.apache.org/)**
* Transformation - **[AWS Glue](https://aws.amazon.com/glue/)**
* Data Storage - **[AWS S3 buckets](https://aws.amazon.com/s3/)**
* Language - **[Python](https://www.python.org/), [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)**
* API - **[News API](https://newsapi.org/)**

### Final Result

![Untitled](https://github.com/sneha-roseline/CloudDataPipeline-Airflow/assets/146040464/9950668c-fe76-4907-94a1-a3a46d19e595)



