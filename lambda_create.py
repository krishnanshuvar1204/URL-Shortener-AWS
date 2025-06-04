import boto3
import json

# AWS Region
region = "ap-south-1"

# Initialize clients
lambda_client = boto3.client("lambda", region_name=region)
iam_client = boto3.client("iam", region_name=region)

# IAM role name and ARN
role_name = "LambdaDynamoDBRole"

# Get IAM Role ARN
role_arn = iam_client.get_role(RoleName=role_name)["Role"]["Arn"]

# Lambda function name
function_name = "URLShortenerFunction"

# Read ZIP file
with open("lambda_function.zip", "rb") as f:
    zip_content = f.read()

# Create Lambda function
response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime="python3.9",
    Role=role_arn,
    Handler="lambda_function.lambda_handler",
    Code={"ZipFile": zip_content},
    Timeout=10,
    MemorySize=128
)

print(json.dumps(response, indent=4))
