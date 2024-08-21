import boto3

def query_has_legal_demand():
    dynamodb = boto3.resource('dynamodb')
    release_table = dynamodb.Table('release')
    pull_request_table = dynamodb.Table('pull_request')

    data = []

    response = release_table.scan()
    
    release_ids = [item['release_id'] for item in response['Items']]
    
    # Obter todos os items da tabela pull_request em lote
    pull_request_items = []
    with pull_request_table.batch_writer() as batch:
        for release_id in release_ids:
            batch.put_item(Item={'release_id': release_id})  # Adiciona os items com release_id na lista de batch

    response_pull_request = pull_request_table.scan()
    pull_request_items = response_pull_request['Items']

    for release_id in release_ids:
        has_legal_demand = any(item.get('has_legal_demand') for item in pull_request_items if item['release_id'] == release_id)

        release_item = [item for item in response['Items'] if item['release_id'] == release_id][0]
        
        data.append({
            'release_id': release_id,
            'version': release_item['version'],
            'has_legal_demand': has_legal_demand
        })

    return {'data': data}

result = query_has_legal_demand()
print(result)