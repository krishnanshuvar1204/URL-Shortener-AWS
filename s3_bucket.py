import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = "myurlbucket-123"

# Create S3 bucket
try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}  # Change to your AWS region
    )
    print(f"S3 bucket '{bucket_name}' created successfully!")
except Exception as e:
    print(f"Error: {e}")