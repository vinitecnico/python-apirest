import json
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    with open('test.json') as f:
        data = json.load(f)
    print(data)
    if data and name:
        return jsonify(data[name])
    elif data:
        return jsonify(data)
    else:
        return jsonify({'error': 'data not found'})

# Carrega o arquivo JSON com as informações da API
with open('api.json') as f:
    api_data = json.load(f)


# Define um dicionário para armazenar as rotas e endpoints
route_endpoints = {}

# Define as rotas e métodos da API com base nas informações do arquivo JSON
for route, methods in api_data.items():
    for method, response_data in methods.items():
        for index, mock_data in enumerate(response_data):
            def create_mock_api(data):
                def mock_api():
                    return jsonify(data['response']), data['status']
                return mock_api

            # Cria um nome exclusivo para a função de visualização
            endpoint_name = f"mock_api_{route}_{method}_{index}"

            # Registra a função de visualização na aplicação Flask
            app.add_url_rule(route, view_func=create_mock_api(mock_data), methods=[method], endpoint=endpoint_name)

            # Armazena a rota e o endpoint no dicionário
            route_endpoints[route] = endpoint_name

# Exibe as rotas e endpoints
for route, endpoint in route_endpoints.items():
    print(f"Rota: {route}")
    print("")



# app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)