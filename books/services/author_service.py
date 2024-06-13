from helpers.logging_helper import logger
from models import Author

class AuthorService:
    def get_author_or_none(self, email: str):
        try:
            user = Author.objects.get(email=email)
        except Exception as e:
            return None
        return user
    
    
    @classmethod
    def get_author_by_email(cls, email):
        user = Author.objects.get(email=email)
        if not user:
            return None
        return user