import requests

def preencher_endereco_por_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        Logradouro = data.get('logradouro')
        Cidade = data.get('localidade')
        Uf = data.get('uf')
        return Logradouro, Cidade, Uf
    else:
        return None, None, None