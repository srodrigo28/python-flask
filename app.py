from flask import Flask

# Criando a aplicação Flask
app = Flask(__name__)

# Criando uma rota
@app.route('/')
def root():
    return 'Olá mundo!'

@app.route('/cadastro')
def submit():
    return '''
        <form method="POST">
            Nome: <input type="text" name="nome" />
            Email: <input type="text" name="email" />
            <input type="submit" value="Enviar" />
        </form>
    '''

# Habilita mostrar erro e porta
if __name__ == '__main__':
    app.run(debug=True, port=5152)