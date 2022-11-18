# Python script to create Amazon Simple Queue Service (SQS) standard queue.
# Import boto3 library
import boto3
# Declare SQS as our resource
sqs = boto3.resource('sqs')
# Pass in our queue name and queue creation method to our variable
queue = sqs.create_queue(QueueName='JW_StandardQueue')
# The new queue's url identifier(required)
print(queue.url)