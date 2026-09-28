from typing import Optional

from sqlalchemy.orm import Session

import models
import schemas


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    """Placeholder: return a list of todos."""
    return []


def get_todo(db: Session, todo_id: int):
    """Placeholder: fetch one todo by id."""
    return None


def create_todo(db: Session, todo: schemas.TodoCreate):
    """Placeholder: create a new todo item."""
    return None


def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    """Placeholder: update an existing todo item."""
    return None


def delete_todo(db: Session, todo_id: int):
    """Placeholder: delete a todo item."""
    return None
