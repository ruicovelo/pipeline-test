import json

def lambda_handler(event, context):
    # TODO implement
    return build_response(200,'Hello from Lambda')


def build_response(status_code, body):
    response = {
        'statusCode': status_code,
        'body': json.dumps(body),
    }
    return response

