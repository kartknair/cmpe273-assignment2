import boto3


def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    item = client.get_item(TableName="pizzaorder", Key=event)
    response = dict()
    response["menu_id"] = item["Item"]["menu_id"]["S"]
    response["order_id"] = item["Item"]["order_id"]["S"]
    response["customer_name"] = item["Item"]["customer_name"]["S"]
    response["customer_email"] = item["Item"]["customer_email"]["S"]
    response["order_status"] = item["Item"]["order_status"]["S"]
    response["order"] = []
    for x in item["Item"]["ordering"]["M"]:
        if x == "costs":
            response["order"].append([x, item["Item"]["ordering"]["M"][x]["N"]])
        else:
            response["order"].append([x, item["Item"]["ordering"]["M"][x]["S"]])
    return response
