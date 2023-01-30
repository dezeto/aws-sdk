start-upload: # start local upload aws
	export PYTHONPATH=. && poetry run python3 src/upload_with_presigned_url_aws.py

start-download: # start local download aws
	export PYTHONPATH=. && poetry run python3 src/download_with_presigned_url_aws.py

start-delete: # start local delete aws
	export PYTHONPATH=. && poetry run python3 src/delete_aws.py

start-download-file: # start local download aws
	export PYTHONPATH=. && poetry run python3 src/download_file_aws.py