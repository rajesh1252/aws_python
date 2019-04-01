import boto3
client = boto3.client('cloudwatch')

def lambda_handler(event, context):
    id = event['detail']['clusterId']
    response = client.put_metric_alarm(
        AlarmName='EMR clusterId is idle for 1hr id = {}'.format(id),
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='IsIdle',
        Namespace='AWS/ElasticMapReduce',
        Period=60,
        Statistic='Average',
        Threshold=0.5,
        ActionsEnabled=True,
        AlarmActions=['arn:aws:sns:us-east-1:921710562778:billing_alerts'],
        AlarmDescription='IsIdle for a min',
        Dimensions=[
            {
                'Name': 'JobFlowId',
                'Value': '{}'.format(id)
            },
        ],
    )
