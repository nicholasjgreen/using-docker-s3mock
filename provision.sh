#!/usr/bin/env bash
echo Creating demo-bucket
aws --endpoint-url=http://localhost:4572 s3 mb s3://demo-bucket
echo Setting up ACL
aws --endpoint-url=http://localhost:4572 s3api put-bucket-acl --bucket demo-bucket --acl public-read
