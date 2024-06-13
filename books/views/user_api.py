from rest_framework.decorators import api_view
from books.helpers.logging_helper import logger
from books.builders.response_builders import ResponseBuilder
from books.serializers.user_login_serializer import AuthorSerializer, AuthorLoginSerializer
from books.services.author_auth_service import AuthorAuthService

@api_view(['POST'])
def register_user(request):
    """
    Register a User and generate Auth Token
    """
    response_builder = ResponseBuilder()
    serialized_data = AuthorSerializer(data=request.data)
    logger.info(f"Serialized data : {serialized_data}")
    if not serialized_data.is_valid():
        return response_builder.result_object({"error": f"Invalid data {serialized_data.errors}"}).fail().bad_request_400().get_response()
    
    email = request.data.get("email")
    password = request.data.get("password")

    if AuthorAuthService().is_email_already_created(email):
        return response_builder.result_object({"error": "A user with this email already exists"}).fail().get_response()
    
    user_obj = serialized_data.save()
    user_auth_service = AuthorAuthService()
    response = {
        "user_data":serialized_data.data,
        "token": user_auth_service.generate_auth_token(user_obj),
    }
    return response_builder.result_object(response).success().ok_200().get_response()


@api_view(['POST'])
def login(request):
    response_builder = ResponseBuilder()
    user_auth_service = AuthorAuthService()
    if not request.method == 'POST':
        return response_builder.result_object({"error": "Invalid Request Method"})
    
    serializer = AuthorLoginSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.result_object({"error": f"Error occured :: {serializer.errors}"}).fail().bad_request_400().get_response()

    email = serializer.validated_data.get("email")
    password = serializer.validated_data.get("password")
    logger.info(f"Email: {email}  :: Password: {password}")
    is_logged_in, auth_token = user_auth_service.login(email, password)

    if not is_logged_in:
        return response_builder.message("Incorrect Email or Password").fail().bad_request_400().get_response()
    
    response = {
        'auth_token': auth_token
    }
    return response_builder.result_object(response).message("User Logged in Succesfully").success().ok_200().get_response()