import boto3
import json

# Initialize the Boto3 client for Lambda
lambda_client = boto3.client('lambda', region_name="ap-south-1")

# Correct Lambda function name
LAMBDA_FUNCTION_NAME = "ShortenURLFunction"

def get_short_url(long_url):
    """Invoke Lambda function to get a short URL."""
    payload = {"long_url": long_url}

    try:
        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )

        # Read and parse the response
        response_payload = json.loads(response['Payload'].read().decode('utf-8'))

        # Print full response for debugging
        print("Lambda Response:", response_payload)

        # Check if "body" exists in response
        if "body" in response_payload:
            body = json.loads(response_payload["body"])
            return body.get("short_url", "Error: short_url not found")
        else:
            return f"Error: {response_payload.get('error', 'Unknown error')}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Test the function
if __name__ == "__main__":
    long_url = "https://example.com"
    short_url = get_short_url(long_url)
    print(f"Short URL: {short_url}")