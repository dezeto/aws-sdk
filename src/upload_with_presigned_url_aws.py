import boto3
from botocore.client import Config
from config import BUCKET_NAME, KEY_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, SIGNATURE_VERSION, EXPIRE_TIME

s3 = boto3.resource(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version=SIGNATURE_VERSION),
    region_name=REGION_NAME
)

# if file name already exist will replace existing file
url = s3.meta.client.generate_presigned_url(
    ClientMethod="put_object",
    Params={
        "Bucket": BUCKET_NAME,
        "Key": KEY_NAME,
    },
    ExpiresIn=EXPIRE_TIME)

print(url)