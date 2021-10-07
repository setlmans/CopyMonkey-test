import boto3
import json
import time

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_request')
    print("Received event: " + json.dumps(event))
    message = json.loads(event['body'])['message']

    table.put_item(
        Item={
            'store': 'messages',
            'message': message,
            'unix_time': int(time.time())

        }
    )
    return {
        'statusCode': 200,
        'body': "written"
    }
