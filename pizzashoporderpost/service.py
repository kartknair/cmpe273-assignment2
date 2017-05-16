import boto3
import json


def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    try:
        client.put_item(TableName="pizzaorder",
                        Item={"order_id":{"S":event["order_id"]},
                              "menu_id":{"S":event["menu_id"]},
                              "customer_name":{"S":event["customer_name"]},
                              "customer_email":{"S":event["customer_email"]},
                              "order_status":{"S":"selecting"},
                              "ordering":{"M":{}}})
        menu = client.get_item(TableName="pizzashoptab", Key={"menuId":{"S":event["menu_id"]}})
        response = "Hi "+event["customer_name"]+", please choose one of these selection: "
        i = 1
        for item in menu["Item"]["selection"]["L"]:
            response = response + str(i) + ". " + item["S"]
            if i < len(menu["Item"]["selection"]["L"]):
                response = response + ", "
            i = i + 1
    except Exception, e:
        return 400, e
    return 200, "OK", {"Message":response}