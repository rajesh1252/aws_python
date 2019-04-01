import boto3
sns = boto3.client('sns')


def lambda_handler(event, context):
    sns.publish(TopicArn='arn:aws:sns:us-east-1:921710562778:billing_alerts',
                    Message='AWS billing alert',Subject='This is a test alert from AWS')
