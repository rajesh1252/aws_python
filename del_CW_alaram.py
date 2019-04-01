
import boto3

client = boto3.client('cloudwatch')

response = client.delete_alarms(
    AlarmNames=[
        'test1-emr',
    ]
)
