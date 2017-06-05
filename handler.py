import json


def endpoint(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response
