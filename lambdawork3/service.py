import boto3


def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    
    try:
        client.update_item(TableName="pizzashoptab", Key=event, 
                           UpdateExpression="SET #sel = list_append(#sel, :val1)",
                           ExpressionAttributeNames={"#sel": "selection"},
                           ExpressionAttributeValues={":val1":{"L":[{"S":"Vegetable"}]}})
        entry = client.get_item(TableName="pizzashoptab", Key=event)
        putresponse = {}
        putresponse ["menuId"] = entry["Item"]["menuId"]["S"]
        putresponse ["selection"] = [select["S"] for select in entry["Item"]["selection"]["L"]]
    except Exception,e:
        return 400, e
    return putresponse, 200, "OK"
