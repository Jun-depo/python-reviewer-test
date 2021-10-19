import boto3

def syncTables(event, context):
    source_ddb = boto3.client('dynamodb', 'us-east-1')
    destination_ddb = boto3.client('dynamodb', 'us-west-2')
    sync_ddb_table(source_ddb, destination_ddb)

# Scan returns paginated results, so only partial data will be copied
def sync_ddb_table(source_ddb, destination_ddb):

    response = source_ddb.scan(TableName="<FMI1>")

    paginator = response.get_paginator('list_items')

    page_iterator = paginator.paginate()

    for page in page_iterator:
        for item in page['Items']:
            destination_ddb.put_item(TableName="<FMI2>", Item=item)
