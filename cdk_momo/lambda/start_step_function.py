import json
import boto3

step_function_client = boto3.client("stepfunctions")


def handler(event, context):
    print("Lambda function invoked")
    print(json.dumps(event))
    print(json.dumps(event["arguments"]['input']))

    response = step_function_client.start_execution(
        stateMachineArn=event["arguments"]['input']['arn'],
        name=event["arguments"]['input']['id'],
        input="{\"details\":{\"accountId\":\"1234567\",\"bookedStatus\":\"Booked\"}}",

    )

    return {"id": event["arguments"]['input']['id'], "arn": event["arguments"]['input']['arn']}
