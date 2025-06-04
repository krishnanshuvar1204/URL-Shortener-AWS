import json
import boto3
import random
import string

# Initialize DynamoDB client
dynamodb = boto3.client("dynamodb", region_name="ap-south-1")

# Function to generate a random short URL key
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    body = json.loads(event["body"]) if "body" in event else event

    if "long_url" not in body:
        return {"statusCode": 400, "body": json.dumps({"error": "Missing 'long_url' in request body"})}

    long_url = body["long_url"]
    short_code = generate_short_code()

    # Store in DynamoDB
    dynamodb.put_item(
        TableName="ShortenedURLs",
        Item={
            "short_url": {"S": short_code},
            "long_url": {"S": long_url}
        }
    )

    short_url = f"https://yourdomain.com/{short_code}"  # Replace with your domain

    return {
        "statusCode": 200,
        "body": json.dumps({"short_url": short_url})
    }
