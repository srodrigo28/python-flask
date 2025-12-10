import requests

# Teste de requisição POST para o servidor Flask
response = requests.post(
    'http://127.0.0.1:5000/submit',  # Porta padrão do Flask
    data={'nome': 'Programador Aventureiro'}
)
print(response.text)
