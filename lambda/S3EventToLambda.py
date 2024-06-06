import json

def lambda_handler(event, context):
    for record in event['Records']:
        print(f"Bucket: {record['s3']['bucket']['name']}, Key: {record['s3']['object']['key']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed S3 event.')
    }

