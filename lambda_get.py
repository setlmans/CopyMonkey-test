import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_request')
    store = 'messages'
    response = table.query(
        KeyConditionExpression=Key('store').eq(store),
        Limit=10,
        ScanIndexForward=False
    )
    ### print(type(response))
    return response['Items']

