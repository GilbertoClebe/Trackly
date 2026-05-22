from models.chat_model import Chat
from repository.chat_repository import ChatRepository
from schemas.chat_schema import Prompt, Response

class ChatService :
    def __init__(self, repo: ChatRepository) :
        self.repo = repo
        
    def save_history(self, prompt: Prompt, response: Response ) -> bool :
        return self.repo.save_history(self.join(prompt, response))
    
    def list_history(self) -> list[Chat] :
        return self.repo.list_history()
    
    def join(self, prompt: Prompt, response: Response) -> Chat :
        return Chat(
            prompt = prompt.prompt,
            message = response.message
        )