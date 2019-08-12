import layerOne
import json


def hello(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Layer responded with: %s' % (layerOne.custom_function(), ),
            'input': event
        })
    }
