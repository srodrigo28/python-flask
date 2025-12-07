from flask import Flask, request
import threading
import time
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return 'Olá mundo!'

@app.route('/cadastro', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form['nome']
        return f'Você enviou: {data}'
    return '''
        <form method="POST">
            Nome: <input type="text" name="nome" />
            <input type="submit" value="Enviar" />
        </form>
    '''

def run_server():
    app.run(debug=True, port=5152)

# Inicia servidor em uma thread separada
threading.Thread(target=run_server, daemon=True).start()

# Aguarda o servidor iniciar
time.sleep(1)

response = requests.post(
    'http://127.0.0.1:5152/cadastro',
    data={'nome': 'Programador Aventureiro'}
)
print(response.text)
