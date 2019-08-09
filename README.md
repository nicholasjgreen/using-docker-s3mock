# using-docker-s3mock
This is me trying out the adobe mock of S3

# You will need
* docker
* python3
* virtual environment

# To bring up the stack

```bash
docker-compose up -d
```

You can check that the buckets have been created like this:
```bash
ls -la s3_temp_files
```

# Set up virtualenv and boto3
```bash
virtualenv s3mock
source s3mock/bin/activate
pip3 install boto3
```

# Run the example
```bash
python3 trys3mock.py
``` 
