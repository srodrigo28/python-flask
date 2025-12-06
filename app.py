from flask import Flask, request

# Criando a aplicação Flask
app = Flask(__name__)

# Criando uma rota responde tipo GET por padrão
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

# Habilita mostrar erro e porta
if __name__ == '__main__':
    app.run(debug=True, port=5152)