import custom_func as cf

def lambda_handler(event, context):
    cf.custom_function()
    return {
        'statusCode': 200,
        'body': 'Layer responded with: %s' % (cf.custom_function(), )
    }
