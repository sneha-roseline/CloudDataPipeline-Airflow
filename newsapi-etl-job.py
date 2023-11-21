import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1696889249641 = glueContext.create_dynamic_frame.from_catalog(
    database="newsapisource-db",
    table_name="landings3bucket_sneha",
    transformation_ctx="AWSGlueDataCatalog_node1696889249641",
)

# Script generated for node Change Schema
ChangeSchema_node1696889457402 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1696889249641,
    mappings=[
        ("newstitle", "string", "newstitle", "string"),
        ("timestamp", "string", "timestamp", "timestamp"),
        ("url_source", "string", "url_source", "string"),
        ("content", "string", "content", "string"),
        ("source", "string", "source", "string"),
        ("author", "string", "author", "string"),
        ("urltoimage", "string", "urltoimage", "string"),
    ],
    transformation_ctx="ChangeSchema_node1696889457402",
)

# Script generated for node Amazon S3
AmazonS3_node1696889512017 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1696889457402,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://destinations3bucket-sneha/newsdata-csv/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1696889512017",
)

job.commit()
