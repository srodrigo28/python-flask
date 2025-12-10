from flask import Flask, request
# import threading
# import requests


app = Flask(__name__)

@app.route('/')
def root():
    # Rota principal retorna uma mensagem simples
    return 'Olá mundo!'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # Rota para envio de dados via formulário
    if request.method == 'POST':
        data = request.form['nome']
        return f'Você enviou: {data}'
    # Exibe formulário HTML para envio do nome
    return '''
        <form method="POST">
            Nome: <input type="text" name="nome" />
            <input type="submit" value="Enviar" />
        </form>
    '''


# Para garantir que o servidor rode na porta correta (5000),
# adicione o bloco abaixo ao final do arquivo:
if __name__ == "__main__":
    app.run(port=5000)
