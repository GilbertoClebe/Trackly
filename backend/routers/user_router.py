from fastapi import APIRouter, Depends
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from services.user_service import UserService
from dependencies import get_user_service
router = APIRouter(tags=(["User"]))

@router.post("/user", response_model=bool)
def create_user(schema: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(schema)

@router.get("/user/{id}", response_model=UserResponse)
def get_user(id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(id)

@router.get("/user", response_model=list[UserResponse])
def list_user(service: UserService = Depends(get_user_service)):
    return service.list_users()

@router.put("/user/{id}", response_model=UserResponse)
def update_user(id: int, schema: UserUpdate, service: UserService = Depends(get_user_service)):
    return service.update_user(id, schema)

@router.patch("/user/deactivate/{id}", response_model=bool)
def deactivate_user(id: int, service: UserService = Depends(get_user_service)):
    return service.deactivate_user(id)