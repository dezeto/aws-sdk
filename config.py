import os

import dotenv

dotenv.load_dotenv(verbose=True)

BUCKET_NAME = os.getenv("BUCKET_NAME")
KEY_NAME = os.getenv("KEY_NAME")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
SIGNATURE_VERSION = os.getenv("SIGNATURE_VERSION")
REGION_NAME = os.getenv("REGION_NAME")
EXPIRE_TIME = os.getenv("EXPIRE_TIME")

OBJECT_MULTI_PART_UPLOAD_ID = os.getenv("OBJECT_MULTI_PART_UPLOAD_ID")
OBJECT_MULTI_PART_PART_NUMBER = int(os.getenv("OBJECT_MULTI_PART_PART_NUMBER"))
