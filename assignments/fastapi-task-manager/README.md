# 📘 Assignment: FastAPI Task Manager

## 🎯 Objective

Construa uma API REST para gerenciar tarefas, aplicando FastAPI, Pydantic, operações CRUD e respostas de erro HTTP em um projeto completo.

## 📝 Tasks

### 🛠️ Definir o Modelo de Tarefa

#### Descrição

Defina um modelo Pydantic chamado `Task` para representar uma tarefa e inicialize uma coleção em memória.

#### Requisitos

O programa concluído deve:

- Definir os campos `title` do tipo `str`, `completed` do tipo `bool` com valor padrão `False` e `priority` com valores `low`, `medium` ou `high`.
- Usar Pydantic para validar automaticamente os dados recebidos.
- Manter tarefas em uma lista chamada `tasks` durante a execução do servidor.

### 🛠️ Listar e Criar Tarefas

#### Descrição

Implemente as rotas para listar todas as tarefas e criar uma nova tarefa.

#### Requisitos

O programa concluído deve:

- Definir `GET /tasks` e retornar todas as tarefas.
- Permitir o parâmetro opcional de consulta `completed` do tipo `bool` em `GET /tasks`.
- Quando `completed` for informado, retornar somente as tarefas com esse estado.
- Definir `POST /tasks` e adicionar a nova tarefa à lista.
- Retornar a tarefa criada com status `201 Created`.
- Retornar erro `422` automaticamente quando os dados forem inválidos.

Exemplo de corpo da requisição:

```json
{
  "title": "Estudar FastAPI",
  "completed": false,
  "priority": "high"
}
```

### 🛠️ Atualizar e Concluir Tarefas

#### Descrição

Implemente uma rota que atualize uma tarefa existente pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Definir `PUT /tasks/{task_id}` com `task_id` do tipo `int`.
- Receber um modelo Pydantic para atualizar os dados da tarefa.
- Substituir a tarefa existente pelo conteúdo recebido.
- Retornar a tarefa atualizada.
- Lançar `HTTPException` com status `404` quando `task_id` não existir.

### 🛠️ Excluir Tarefas com Segurança

#### Descrição

Finalize a API permitindo excluir tarefas e garantindo uma resposta clara quando o identificador não existir.

#### Requisitos

O programa concluído deve:

- Definir `DELETE /tasks/{task_id}`.
- Remover a tarefa correspondente da lista.
- Retornar a tarefa removida em formato JSON.
- Lançar `HTTPException` com status `404` e uma mensagem clara em `detail` quando o identificador não existir.
