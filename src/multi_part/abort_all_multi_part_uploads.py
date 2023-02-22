import boto3
from botocore.client import Config

from config import (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME,
                    KEY_NAME, REGION_NAME, SIGNATURE_VERSION)

s3 = boto3.resource(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version=SIGNATURE_VERSION),
    region_name=REGION_NAME,
)

multipart_uploads = s3.meta.client.list_multipart_uploads(
    Bucket=BUCKET_NAME,
)

aborted = []
print("Aborting", len(multipart_uploads), "uploads")
if "Uploads" in multipart_uploads:
    for u in multipart_uploads["Uploads"]:
        upload_id = u["UploadId"]
        aborted.append(
            s3.meta.client.abort_multipart_upload(
                Bucket=BUCKET_NAME, Key=KEY_NAME, UploadId=upload_id
            )
        )
print(aborted)
