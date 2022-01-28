# To get a list of all buckets

import boto3

def get_list_buckets():
    boto_session= boto3.session.Session()
    boto_s3_client = boto_session.client('s3')

    try:
        boto_bucket_list = boto_s3_client.list_buckets()
        boto_buckets =[]
        for boto_bucket in boto_bucket_list['Buckets']:
            boto_buckets += {boto_bucket["Name"]}

    except:
        print("Could not open AWS session to bucket list.")
        return
            
            
    return boto_buckets

print(get_list_buckets())





