from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
from database import Base, SessionLocal, engine, get_db
from schemas import Todo, TodoCreate, TodoUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Todo API is running"}


@app.post("/todos/", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Placeholder: create a new todo item."""
    return crud.create_todo(db=db, todo=todo)


@app.get("/todos/", response_model=list[Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Placeholder: return the list of todos."""
    return crud.get_todos(db=db, skip=skip, limit=limit)


@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Placeholder: return one todo by id."""
    todo = crud.get_todo(db=db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    """Placeholder: update a todo item."""
    updated_todo = crud.update_todo(db=db, todo_id=todo_id, todo=todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Placeholder: delete a todo item."""
    deleted = crud.delete_todo(db=db, todo_id=todo_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
