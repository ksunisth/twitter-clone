import os
import boto3

local_host = "http://localhost:8000"
DYNAMODB_ENDPOINT = os.environ.get("DYNAMODB_ENDPOINT", local_host)

dynamodb = boto3.resource("dynamobd", endpoint_url=DYNAMODB_ENDPOINT)
