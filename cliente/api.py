import requests

def preencher_endereco_por_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logradouro = data.get('logradouro')
        cidade = data.get('localidade')
        uf = data.get('uf')
        return logradouro, cidade, uf
    else:
        return None, None, None