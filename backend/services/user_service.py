from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from models.user_model import User
class UserService :
    def __init__(self, repo: UserRepository) :
        self.repo = repo
        
    def create_user(self, schema: UserCreate) -> bool :
        user = self.parse_create_to_user(schema)
        return self.repo.create_user(user)
    
    def get_user(self, id: int) -> User :
        return self.repo.get_user(id)
    
    def list_users(self) -> list[User] :
        return self.repo.list_user()
    
    def update_user(self, id: int, schema: UserUpdate) -> User :
        new_data = self.parse_update_to_user(schema)
        user = self.get_user(id)

        for field in ["name", "email", "number", "CPF", 
                      "address", "role" ,"date_creation" ,"active"] :
            
            value = getattr(new_data, field)
            
            if value is not None :
                setattr(user, field, value)
        return self.repo.update_user(user)
    
    def deactivate_user(self, id) -> bool :
        return self.repo.deactivate_user(id)
    
    def parse_create_to_user(self, schema: UserCreate) -> User :
        return User(
            name = schema.name,
            email = schema.email,
            number = schema.number,
            CPF = schema.CPF,
            address = schema.address,
            role = schema.role.value
        )
        
    def parse_update_to_user(self, schema: UserUpdate) -> User :
        return User(
            name = schema.name,
            email = schema.email,
            number = schema.email,
            CPF = schema.CPF,
            address = schema.address,
            role = schema.role.value,
            date_creation = schema.date_creation,
            active = schema.active
        )
        
    