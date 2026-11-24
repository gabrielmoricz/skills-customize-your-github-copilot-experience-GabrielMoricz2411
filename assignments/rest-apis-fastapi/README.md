# 📘 Atividade: Construindo REST APIs com FastAPI

## 🎯 Objetivo

Criar uma API REST simples com FastAPI, praticando rotas, parâmetros, validação de dados com Pydantic e respostas de erro HTTP.

## 📝 Tarefas

### 🛠️ Primeira Rota

#### Descrição
Crie uma rota `GET /` que retorne uma mensagem de boas-vindas em formato JSON.

#### Requisitos
O programa concluído deve:

- Definir a rota `GET /` com o decorador `@app.get("/")`.
- Retornar um dicionário com a chave `"message"`.
- Exemplo de resposta:
  ```json
  {"message": "Welcome to my API!"}
  ```

### 🛠️ Rota com Parâmetro de Caminho

#### Descrição
Crie uma rota `GET /items/{item_id}` que retorne um item da lista `items` pelo seu índice.

#### Requisitos
O programa concluído deve:

- Receber `item_id` como parâmetro de caminho do tipo `int`.
- Retornar o item correspondente da lista `items`.
- Exemplo de uso: `GET /items/0` retorna o primeiro item cadastrado.

### 🛠️ Criação de Itens com Validação

#### Descrição
Crie uma rota `POST /items` que receba um item no corpo da requisição, valide os dados com um modelo Pydantic e adicione-o à lista `items`.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Item` com os campos `name` (texto) e `price` (número decimal).
- Receber o item no corpo da requisição em JSON.
- Adicionar o item à lista `items` e retornar o item criado.
- Retornar automaticamente erro `422` quando algum campo estiver ausente ou com tipo inválido.
- Exemplo de corpo da requisição:
  ```json
  {"name": "Caderno", "price": 12.5}
  ```

### 🛠️ Tratamento de Erros

#### Descrição
Ajuste a rota `GET /items/{item_id}` para tratar índices que não existem na lista.

#### Requisitos
O programa concluído deve:

- Lançar `HTTPException` com status `404` quando `item_id` não existir na lista `items`.
- Incluir uma mensagem de erro clara no campo `detail` da resposta.
- Continuar retornando o item normalmente quando o índice existir.
