from typing import Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task Manager API")


class Task(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False
    priority: Literal["low", "medium", "high"] = "medium"


tasks: list[dict] = [
    {"id": 1, "title": "Ler a documentação do FastAPI", "completed": True, "priority": "medium"},
    {"id": 2, "title": "Criar uma rota POST", "completed": False, "priority": "high"},
]


# Tarefa 1: os dados iniciais já estão preparados. Valide novas tarefas com a classe Task.

# Tarefa 2: implemente GET /tasks e adicione o filtro opcional completed.

# Tarefa 3: implemente POST /tasks e retorne status 201.

# Tarefa 4: implemente PUT /tasks/{task_id}.

# Tarefa 5: implemente DELETE /tasks/{task_id}.
