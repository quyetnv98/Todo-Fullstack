from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.models import Todo
from app.schemas.schemas import TodoCreate, TodoUpdate, TodoResponse
from app.crud import crud_todo

router = APIRouter()

@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    # TODO: Gọi hàm crud_todo.create_todo() để tạo mới Todo. Trả về đối tượng vừa tạo.
    pass

@router.get("/", response_model=List[TodoResponse])
def read_todos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    # TODO: Gọi hàm crud_todo.get_todos() để lấy danh sách Todo. Trả về danh sách đó.
    pass

@router.get("/{todo_id}", response_model=TodoResponse)
def read_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    # TODO: Gọi hàm crud_todo.get_todo(). Nếu không tìm thấy, throw HTTPException 404. Trả về kết quả.
    pass

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    db: Session = Depends(get_db)
):
    # TODO: Lấy todo từ CSDL. Nếu không có -> lỗi 404. Nếu có -> gọi crud_todo.update_todo().
    pass

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    # TODO: Lấy todo từ CSDL. Nếu không có -> lỗi 404. Nếu có -> gọi crud_todo.delete_todo(). Trả về None.
    pass
