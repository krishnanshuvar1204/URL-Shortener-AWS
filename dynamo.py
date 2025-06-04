import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb', region_name="ap-south-1")

# Define table parameters
table_name = "ShortenedURLs"

try:
    # Create the table
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {"AttributeName": "ShortURL", "KeyType": "HASH"}  # Partition key
        ],
        AttributeDefinitions=[
            {"AttributeName": "ShortURL", "AttributeType": "S"}  # String type
        ],
        BillingMode="PAY_PER_REQUEST",  # On-demand mode (no need to set RCU/WCU)
    )

    print(f"Table {table_name} is being created...")
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table {table_name} already exists.")