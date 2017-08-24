import boto3

s3 = boto3.resource('s3')
s3client = boto3.client('s3')

response = s3client.list_buckets()
print(response)
for bucket in response["Buckets"]:
    # Create a paginator to pull 1000 objects at a time
    paginator = s3client.get_paginator('list_objects')
    pageresponse = paginator.paginate(Bucket=bucket["Name"])
    
    # PageResponse Holds 1000 objects at a time and will continue to repeat in chunks of 1000. 
    for pageobject in pageresponse:
        for file in pageobject["Contents"]:
            print(file["Key"])
