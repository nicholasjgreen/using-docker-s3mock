import boto3

# Create an S3 client pointed at the localhost. The credentials are totally made up
session = boto3.session.Session()
endpointurl = "http://localhost:4572"
s3_client = session.client(service_name = "s3", aws_access_key_id="a", aws_secret_access_key="b", endpoint_url=endpointurl)

# List the buckets
print("Retrieving buckets")
buckets = s3_client.list_buckets()["Buckets"]
print("Buckets found:")
for bucket in buckets:
    print("*  ", bucket["Name"])
print()

# Upload a file
filename = "trys3mock.py"
bucketname = buckets[0]["Name"]
print("Uploading", filename, "to", bucketname)
s3_client.upload_file(filename, bucketname, "file1.py")
s3_client.upload_file(filename, bucketname, "file2.py")
s3_client.upload_file(filename, bucketname, "file3.py")
print("Upload complete")
print()

print("Retrieving list of keys from ", bucketname)
kwargs = {'Bucket': bucketname, 'Prefix': ''}
resp = s3_client.list_objects(**kwargs)
for obj in resp['Contents']:
    print("*  ", obj['Key'])
print()

print("Retrieving a file from S3")
obj = s3_client.get_object(Bucket=bucketname, Key="file1.py")
content = obj['Body'].read().decode('utf-8').splitlines()
print("Printing first 10 lines:")
for line in content[:10]:
    print(">   ", line)
print()

print("All done!")
