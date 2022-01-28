# Script to create bucket and list all buckets

import boto3_s3_bucket_tools
import json

# Create s3 bucket
print ("Bucket " + boto3_s3_bucket_tools.create_s3_bucket("todbucket-") + " created.")

# Print bucket list
print ("Bucket List:")
print (json.dumps(boto3_s3_bucket_tools.get_list_buckets(), indent=4))

# Delete first bucket
boto3_s3_bucket_tools.remove_first_bucket(boto3_s3_bucket_tools.get_list_buckets())

# Print bucket list
print ("New Bucket List:")
print (json.dumps(boto3_s3_bucket_tools.get_list_buckets(), indent=4))

