import boto3

def create_ebs_volume(size, availability_zone, volume_type='gp2', region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)

    try:
        response = ec2.create_volume(
            Size=size,
            AvailabilityZone=availability_zone,
            VolumeType=volume_type
        )
        volume_id = response['VolumeId']
        print(f"EBS Volume {volume_id} created in {availability_zone}")
        print(response)
        return volume_id
    except Exception as e:
        print(f"Error creating volume: {e}")
        return None

def attach_ebs_volume(instance_id, volume_id, device_name, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)

    try:
        response = ec2.attach_volume(
            Device=device_name,
            InstanceId=instance_id,
            VolumeId=volume_id
        )
        print(f"EBS Volume {volume_id} attached to {instance_id} on {device_name}")
        print(response)
    except Exception as e:
        print(f"Error attaching volume: {e}")

# Example usage
if __name__ == "__main__":
    region = "ap-south-1"  # Change to your AWS region
    size = 10  # Size in GB
    availability_zone = "ap-south-1b"  # Replace with your AZ
    volume_type = "gp2"  # Change volume type if needed

    volume_id = create_ebs_volume(size, availability_zone, volume_type, region)

    if volume_id:
        instance_id = "i-054d981dfe25e00ba"
        device_name = "/dev/xvdbf"
        attach_ebs_volume(instance_id, volume_id, device_name, region)