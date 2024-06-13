from rest_framework_simplejwt.tokens import RefreshToken
from .author_service import AuthorService
from books.helpers.logging_helper import logger
from books.helpers.auth_utils import check_password, hash_raw_password

author_service = AuthorService()
class AuthorAuthService:

    def check_password(email: str, password: str) -> bool:
        user_obj = author_service.get_author_or_none(email=email)
        
    
    def is_email_already_created(self, email:str) -> bool:
        user = author_service.get_author_or_none(email=email)
        if not user:
            return False
        return True

    @staticmethod
    def generate_auth_token(user_obj):
        refresh = RefreshToken.for_user(user_obj)
        return str(refresh.access_token)

    @staticmethod
    def login(email: str, password: str) -> bool:
        logger.info(f"Check here: Email: {email} Password: {password}")
        user = author_service.get_author_by_email(email=email)
        logger.info(f"Fetched the following user:: {user}")
        if not user:
            return False, ""
        is_password_correct = check_password(raw_password=password, hashed_password=user.password)
        if is_password_correct:
            auth_token = AuthorAuthService.generate_auth_token(user)
            return True, auth_token
        return False, ""
        
