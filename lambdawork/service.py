# -*- Post method for input data in pizzashop -*-
import boto3
import json

def myStringListFormatter(inputList):
    newList = []
    for i in inputList:
        returnMap = {"S" : i}
        newList.append(returnMap)
    return newList


def myNumericListFormatter(inputList):
    newList = []
    for i in inputList:
        returnMap = {"N" : i}
        newList.append(returnMap)
    return newList



def handler(event, context):
    client = boto3.client("dynamodb")
    store_hours = {}

    for entry in event ["store_hours"]:
        i = dict()
        i["S"] = event["store_hours"][entry]
        store_hours[entry] = i


    try:
        client.put_item(TableName="pizzashoptab",
                        Item={"menuId": {"S": event["menu_id"]},
                              "storeName": {"S": event["store_name"]},
                              "selection": {"L": myStringListFormatter(event["selection"])},
                              "size": {"L": myStringListFormatter(event["size"])},
                              "price": {"L": myNumericListFormatter(event["price"])},
                              "storeHours": {"M": store_hours},
                              "sequence": {"L": [{"S": "selection"}, {"S": "size"}]}})
    except Exception,e:
        return 400, e
    return 200, "OK"
