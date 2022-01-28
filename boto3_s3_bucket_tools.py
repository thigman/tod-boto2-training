import boto3
import uuid
from uuid import uuid4
from boto3.session import Session


def bucket_name_generator(bucket_name_prefix):
    return ''.join([bucket_name_prefix, str(uuid.uuid4())])


def create_s3_bucket(bucket_name_prefix):

    try:
        boto_session= boto3.session.Session()
        boto_s3_resource = boto_session.resource('s3', region_name = 'us-west-1')
        bucket_name = bucket_name_generator(bucket_name_prefix)
        boto_s3_resource.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                        'LocationConstraint': 'us-west-1'})
    except:
        print("ERROR: Could not create s3 bucket.")
    
    else:    
        return bucket_name


def get_list_buckets():

    try:
        boto_session= boto3.session.Session()
        boto_s3_client = boto_session.client('s3')
        boto_bucket_list = boto_s3_client.list_buckets()
        boto_buckets =[]
        for boto_bucket in boto_bucket_list['Buckets']:
            boto_buckets += {boto_bucket["Name"]}

    except:
        print("ERROR: Could not open AWS session to list buckets.")
        return
    
    else:
        return boto_buckets

def remove_first_bucket(bucket_list):

    try:
        boto_session= boto3.session.Session()
        boto_s3_client = boto_session.client('s3')
        boto_s3_client.delete_bucket(Bucket=bucket_list[0])
        
    except:
        print("ERROR: Could not delet s3 bucket.")
        return
    
    else:    
        print("Bucket " + bucket_list[0] + " deleted.")
        return