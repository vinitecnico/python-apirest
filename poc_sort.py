import json
import datetime

def sort_data(data):
    def custom_sort(item):
        if item['update_at'] is None:
            update_at = datetime.datetime.strptime(item['create_at'], "%Y-%m-%dT%H:%M:%S")
        else:
            update_at = datetime.datetime.strptime(item['update_at'], "%Y-%m-%dT%H:%M:%S")
        
        history_sorted = sorted(item['history'], key=lambda x: x['valor'], reverse=True)
        
        return (update_at, history_sorted[0]['valor'])

    sorted_data = sorted(data, key=custom_sort, reverse=True)

    for item in sorted_data:
        item['history'] = sorted(item['history'], key=lambda x: x['valor'], reverse=True)

    return sorted_data

data = [
    {
        "id": "123",
        "flavor": "test",
        "create_at": "2024-04-27T10:00:00",
        "update_at": None,
        "history": [
            {
                "valor": 10,
                "create_at": "2024-04-27T10:00:00",
                "update_at": None
            },
            {
                "valor": 25,
                "create_at": "2024-04-27T10:00:00",
                "update_at": None
            },
            {
                "valor": 100,
                "create_at": "2024-04-27T10:00:00",
                "update_at": None
            },
        ]
    },
    {
        "id": "321",
        "flavor": "test",
        "create_at": "2024-04-25T16:00:00",
        "update_at": "2024-04-27T16:00:00",
        "history": [
            {
                "valor": 10,
                "create_at": "2024-04-27T10:00:00",
                "update_at": None
            },
            {
                "valor": 25,
                "create_at": "2024-04-27T10:00:00",
                "update_at": None
            },
            {
                "valor": 100,
                "create_at": "2024-04-27T10:00:00",
                "update_at": None
            },
        ]
    }
]

sorted_data = sort_data(data)

sorted_data_json = json.dumps(sorted_data, indent=4)

print(sorted_data_json)