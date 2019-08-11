import json
import boto3

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='arn:aws:lambda:us-east-1:534451562636:function:Lambdawithlayer',
    InvocationType='RequestResponse',
    LogType='None',
)
payload = json.loads(response['Payload'].read())

print('RESPONSE: %s' % (payload,))
