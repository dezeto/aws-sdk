start-upload: # start local upload aws
	export PYTHONPATH=. && poetry run python3 src/upload_aws.py

start-download: # start local download aws
	export PYTHONPATH=. && poetry run python3 src/download_aws.py

start-delete: # start local delete aws
	export PYTHONPATH=. && poetry run python3 src/delete_aws.py
