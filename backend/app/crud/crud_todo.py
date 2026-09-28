from sqlalchemy.orm import Session
from app.models.models import Todo
from app.schemas.schemas import TodoCreate, TodoUpdate

def get_todo(db: Session, todo_id: int):
    # TODO: Truy vấn CSDL để lấy 1 Todo theo todo_id
    pass

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    # TODO: Truy vấn danh sách Todo, hỗ trợ phân trang bằng skip và limit
    pass

def create_todo(db: Session, todo: TodoCreate):
    # TODO: Khởi tạo đối tượng Todo, thêm vào db, commit và refresh để có ID mới
    pass

def update_todo(db: Session, db_todo: Todo, todo: TodoUpdate):
    # TODO: Lấy dữ liệu từ TodoUpdate và ghi đè vào db_todo. Sau đó commit và refresh
    pass

def delete_todo(db: Session, db_todo: Todo):
    # TODO: Xóa db_todo khỏi CSDL và commit thay đổi
    pass
