import boto3
from botocore.client import Config

from config import (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME,
                    EXPIRE_TIME, KEY_NAME, REGION_NAME, SIGNATURE_VERSION)

s3 = boto3.resource(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version=SIGNATURE_VERSION),
    region_name=REGION_NAME,
)

url = s3.meta.client.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": BUCKET_NAME,
        "Key": KEY_NAME,
    },
    ExpiresIn=EXPIRE_TIME,
)

print(url)
