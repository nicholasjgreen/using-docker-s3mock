import boto3

def get_all_s3_keys(bucket):
    """Get a list of all keys in an S3 bucket."""
    keys = []

    kwargs = {'Bucket': bucket}
    while True:
        resp = s3_client.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            keys.append(obj['Key'])

        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break

    return keys


# Create an S3 client pointed at the localhost. The credentials are totally made up
session = boto3.session.Session()
endpointurl = "http://localhost:9090"
s3_client = session.client(service_name = "s3", aws_access_key_id="a", aws_secret_access_key="b", endpoint_url=endpointurl)

# List the buckets
print(s3_client.list_buckets())
buckets = s3_client.list_buckets()["Buckets"]
print("Buckets found:")
for bucket in buckets:
    print("*  ", bucket["Name"])

# Upload a file
filename = "trys3mock.py"
bucketname = buckets[0]["Name"]
print("Uploading", filename, "to", bucketname)
s3_client.upload_file(filename, bucketname, filename)
print("Upload complete")

print("Retrieving list of keys from ", bucketname)
kwargs = {'Bucket': bucketname, 'Prefix': ''}
resp = s3_client.list_objects(**kwargs)
for obj in resp['Contents']:
    print("*  ", obj['Key'])
