import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Table name
table_name = "ShortenedURLs"

# Scan table and fetch items
response = dynamodb.scan(TableName=table_name)

# Print items
for item in response.get('Items', []):
    print(item)