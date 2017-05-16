import boto3

def handler(event, context):
    client = boto3.client("dynamodb")
    try:
        client.delete_item(TableName="pizzashoptab", Key=event)
    except Exception, e:
        return 400, e
    return 200, "OK"