# Cloud ETL Pipeline with Airflow
 An ETL data pipeline with REST API, AWS, Spark, Airflow and much more!

## Description

The project will fetch news data related to a specific topic using News API by writing an ETL Python script and create a data pipeline that consumes the news data. 
The data coming in will be fetched based on a specific topic chosen to extract in our python script and extract the data in parquet format and directly stored on the AWS S3 landing bucket.
Built an ETL pipeline that would use AWS Glue to to load data from S3 landing bucket. In the ETL batch job, 
AWS glue involves using AWS glue crawler to crawl the data in S3 bucket to infer schemas and create a data catalogue. Transformations are applied and the results are store back to a destination s3 bucket.
Various AWS servcies like S3, EC2, AWS Glue, Data Catalogue, CloudWatch, AWS CLI along with IAMS were used. The entire process of fetching the data and the ETL pipeline was orchestrate using Apache Airflow which was run on AWS EC2 instance.

## Architecture
<img width="1343" alt="Screen Shot 2023-10-18 at 6 57 49 PM" src="https://github.com/sneha-roseline/CloudDataPipeline-Airflow/assets/146040464/21a4ccc3-9910-4022-9cf2-0e9aa64ee89c">

## Tools & Technologies

* Cloud - **[Amazon Web Sevices](https://aws.amazon.com/)**
* Batch Processing - **[Spark](https://spark.apache.org/)**
* Orchestration - **[Airflow](https://airflow.apache.org/)**
* Transformation - **[AWS Glue](https://aws.amazon.com/glue/)**
* Data Storage - **[AWS S3 buckets](https://aws.amazon.com/s3/)**
* Language - **[Python](https://www.python.org/), [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)**
* API - **[News API](https://newsapi.org/)**

## Environment setup & Instructions:

>[!WARNING]
>You will be charged for EC2 and Glue in this project even if you're on your free tier!


***<ins>Step 1:<ins>*** Create an account with News API
Ensure that you have the API key for our Python code to fetch the data.

***<ins>Step 2:<ins>*** Set Up AWS Account
If you don't have an AWS account, sign up for one on the AWS website. Make sure you have your AWS access keys and secret keys ready.

***<ins>Step 3:<ins>*** Install and Configure AWS CLI
If you haven't already, install the AWS Command Line Interface (CLI) on your local machine. After installation, configure it by running aws configure and providing your AWS access keys, secret keys, default region, and output format.

***<ins>Step 4:<ins>*** Create an Amazon Elastic Compute Cloud (EC2) instance with Identity and Access Management (IAM) roles that allow it to interact with Amazon S3
- Log in to the AWS Management Console.
- Launch an EC2 Instance
- Create an IAM Role and attach IAM Role to EC2 Instance, make sure it has AmazonS3FullAccess, AmazonEC2FullAccess, AWSGlueConsoleFullAccess group policies attached.

***<ins>Step 5:<ins>*** Upload the python scripts to an Amazon EC2 instance (in the cloud) 
- Command in terminal: scp -i /path/to/your/key.pem /path/to/your/local/script.py ubuntu@ec2-instance-ip:/path/to/remote/directory/
- Ensure that the news_fetcher_etl.py(python script to fetch data using API) module exists in the same directory as your DAG file (news_automation_dag.py)

***<ins>Step 4:<ins>*** Create S3 Buckets
- Navigate to the S3 service.
- Create two S3 buckets: one for the source data and one for the destination data (if they don't exist). Note down the bucket names.

***<ins>Step 6:<ins>*** Set Up AWS Glue
- Navigate to the AWS Glue service in the AWS Management Console.
- Create a new AWS Glue Crawler to catalog the data in your source bucket
- Specify the data store as the source S3 bucket.
- Choose a database or create a new one for cataloging.
- Run the crawler to discover and catalog the Parquet data.

***<ins>Step 7:<ins>*** Create an AWS Glue ETL Job
- In AWS Glue, create a new ETL (Extract, Transform, Load) job.
- Specify the source (cataloged Parquet data) and destination (S3 bucket) locations.
- Write PySpark code in the ETL script to perform data cleaning and preprocessing.

![Untitled1](https://github.com/sneha-roseline/CloudDataPipeline-Airflow/assets/146040464/302c56fb-c51e-4cbc-a93b-4c57f5d36380)

***<ins>Step 8:<ins>*** Set up an environment for working with Python and Apache Airflow
- Commands to run on AWS CLI:
  - sudo apt update
  - sudo apt install python3-pip
  - sudo apt install python3.10-venv
  - python3 -m venv news_proj
  - source news_proj/bin/activate 
  - sudo pip install apache-airflow
  - pip install apache-airflow-providers-amazon
  - airflow standalone

***<ins>Step 9:<ins>*** Airflow setup
- Navigate to http://your-ec2-instance-ip:port in web browser.
- Sign in to Airflow with the username and password from previous step.
- Establish an AWS S3 connection in the Apache Airflow web interface under Connection Type with AWS Access Key ID and AWS Secret Access Key 

***<ins>Step 10:<ins>*** Turn on the news_automation_dag and run the DAG

## Final Result

![Untitled](https://github.com/sneha-roseline/CloudDataPipeline-Airflow/assets/146040464/9950668c-fe76-4907-94a1-a3a46d19e595)












