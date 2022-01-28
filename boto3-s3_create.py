import boto3
import uuid
from uuid import uuid4
from boto3.session import Session


def bucket_name_generator(bucket_name_prefix):
    return ''.join([bucket_name_prefix, str(uuid.uuid4())])

#sess = Session(region_name='us-west-2')

# use S3 
s3 = boto3.resource('s3', region_name = 'us-west-1')

bucket_name = bucket_name_generator('todbucket-')

s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                        'LocationConstraint': 'us-west-1'})
