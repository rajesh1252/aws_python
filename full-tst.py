import boto3

client = boto3.client('cloudwatch')
id = 'j-28AYYJGATS1IY'
response = client.put_metric_alarm(
    AlarmName='EMR clusterId is idle for 1hr id = {}'.format(id),
    AlarmDescription='test emr',
    EvaluationPeriods=1,
    ActionsEnabled=True,
    AlarmActions=['arn:aws:sns:us-east-1:921710562778:billing_alerts'],
    MetricName='IsIdle',
    Namespace='AWS/ElasticMapReduce',
    Statistic='Average',
    Dimensions=[
        {
            'Name': 'JobFlowId',
            'Value': '{}'.format(id)
        },
    ],
    Period=60,
    Unit='Seconds',
    Threshold=0.5,
    ComparisonOperator='GreaterThanOrEqualToThreshold',
)
