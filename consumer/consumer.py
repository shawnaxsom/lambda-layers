import boto3

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='string',
    InvocationType='RequestResponse',
    LogType='Tail',
    ClientContext='string',
    Payload=b'bytes',
    Qualifier='string'
)

