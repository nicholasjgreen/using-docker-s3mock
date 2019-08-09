# using-docker-s3mock
This is me trying out the mock of S3 based on localstack

# You will need
* docker
* python3
* virtual environment

# To bring up the stack

```bash
docker-compose up -d
./provision.sh
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
