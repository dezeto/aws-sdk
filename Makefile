start-upload: # start local upload aws
	export PYTHONPATH=. && poetry run python3 src/upload_with_presigned_url_aws.py

start-multi-part-upload: # start local multi upload aws
	export PYTHONPATH=. && poetry run python3 src/multi_part/start_multi_part_upload_aws_sdk.py

start-generate-multi-part-upload-presigned-url: # start generate presigned url local multi upload aws
	export PYTHONPATH=. && poetry run python3 src/multi_part/generate_multi_part_upload_presigned_url.py

start-abort-all-multi-part-upload:  # start aborting all multi upload process
	export PYTHONPATH=. && poetry run python3 src/multi_part/abort_all_multi_part_uploads.py

start-complete-multi-part-upload: # start completing  multi upload process
	export PYTHONPATH=. && poetry run python3 src/multi_part/complete_multi_part_upload.py

start-download: # start local download aws
	export PYTHONPATH=. && poetry run python3 src/download_with_presigned_url_aws.py

start-delete: # start local delete aws
	export PYTHONPATH=. && poetry run python3 src/delete_aws.py

start-download-file: # start local download aws
	export PYTHONPATH=. && poetry run python3 src/download_file_aws.py

format-all: # run black and isort ignoring migration package and gitignored files
	poetry run black --extend-exclude="database/" . && poetry run isort --extend-skip-glob="database/*" .