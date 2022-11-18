# Lambda Function to send Msg w/ timestamp to SQS
# Import Libraries
import json
import boto3
from datetime import datetime
# Define Function and pass current date and time to variables  
def lambda_handler(event, context):
    now = datetime.now()
    time_date = now.strftime("%H:%M:%S %m/%d/%y")
# Use low-level client and send_message method to deliver msg to specified queue   
    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/514918191735/JW_StandardQueue",
        MessageBody=time_date
    )
    # Returns dictionary object
    return {
        'statusCode': 200,
        'body': json.dumps('time_date')
    }