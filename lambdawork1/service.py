import boto3


def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    response = client.get_item(TableName="pizzashoptab", Key=event)
    store_hours = []
    for item in response["Item"]["storeHours"]["M"]:
        store_hours.append([item, response["Item"]["storeHours"]["M"][item]["S"]])
    response["Item"]["storeHours"] = store_hours
    return response
