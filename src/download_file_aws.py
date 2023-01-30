import boto3
from botocore.client import Config
from config import BUCKET_NAME, KEY_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, SIGNATURE_VERSION
import os

s3 = boto3.resource(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version=SIGNATURE_VERSION),
    region_name=REGION_NAME
)


with open(f'{os.getcwd()}/files/test', 'wb') as data:
    s3.meta.client.download_file(BUCKET_NAME, KEY_NAME, data.name)
    data.close()
    os.unlink(data.name)
