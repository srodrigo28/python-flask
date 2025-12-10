# Guia: Flask + Supabase - CRUD de Tarefas

Este guia mostra como criar um app TODO usando Flask (backend) e Supabase (banco de dados). O app permite cadastrar tarefas, descrição, status e datas, realizando um CRUD completo.

## Pré-requisitos
- Python instalado
- Conta no Supabase (https://supabase.com/)
- Flask e supabase-py instalados

## Passos

### 1. Criar projeto no Supabase
- Acesse o painel do Supabase e crie um novo projeto.
- No menu "Table Editor", crie uma tabela chamada `tasks` com os campos:
  - `id` (integer, primary key, auto increment)
  - `title` (text)
  - `description` (text)
  - `status` (text)
  - `due_date` (date)

### 2. Obter credenciais da API
- No Supabase, vá em "Project Settings" > "API".
- Copie a `URL` e a `anon key`.

### 3. Instalar dependências
```bash
pip install flask supabase-py
```

### 4. Criar o backend Flask
- Crie um arquivo `app.py` com rotas para cada operação CRUD:
  - **Criar tarefa** (POST)
  - **Listar tarefas** (GET)
  - **Atualizar tarefa** (PUT/PATCH)
  - **Excluir tarefa** (DELETE)

### 5. Exemplo de código Flask + Supabase
```python
from flask import Flask, request, jsonify
from supabase import create_client, Client

app = Flask(__name__)

SUPABASE_URL = 'sua_url_aqui'
SUPABASE_KEY = 'sua_anon_key_aqui'
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    res = supabase.table('tasks').select('*').execute()
    return jsonify(res.data)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    res = supabase.table('tasks').insert([data]).execute()
    return jsonify(res.data)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    res = supabase.table('tasks').update(data).eq('id', task_id).execute()
    return jsonify(res.data)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    res = supabase.table('tasks').delete().eq('id', task_id).execute()
    return jsonify(res.data)

if __name__ == '__main__':
    app.run(debug=True)
```

### 6. Testar as rotas
- Use ferramentas como Postman ou Insomnia para testar as rotas:
  - `GET /tasks` para listar
  - `POST /tasks` para criar
  - `PUT /tasks/<id>` para atualizar
  - `DELETE /tasks/<id>` para excluir

### 7. Melhorias
- Adicione validação de dados.
- Implemente autenticação se necessário.
- Crie uma interface web ou mobile para consumir a API.

---
Este guia cobre o básico para um CRUD de tarefas usando Flask e Supabase. Adapte conforme sua necessidade!