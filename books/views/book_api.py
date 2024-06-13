from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from books.builders.response_builders import ResponseBuilder
from books.services.book_service import BookService
from books.services.review_service import ReviewService
from books.helpers.logging_helper import logger
from books.permissions import IsLoggedIn, is_user_or_admin


@api_view(['GET', 'POST'])
@permission_classes([IsLoggedIn])
def book_list(request):
    response_builder = ResponseBuilder()
    book_service = BookService()
    paginator = PageNumberPagination()
    if request.method == 'GET':
        try:
            books = book_service.get_all_book(request=request)
            result_page = paginator.paginate_queryset(books, request)
            return response_builder.get_200_success_response(message="Books Fetched successfully",result=result_page)
            
        except Exception as e:
            logger.error(f"BookView get :: exception::  {e}")
            return response_builder.get_400_bad_request_response(error_code=1, errors=f"{e}")

    if request.method == 'POST':
        book, is_book_created = book_service.create_new_book(data=request.data)
        if is_book_created:
            return response_builder.get_200_success_response(message="Book Created Successfully",result=book)
        return response_builder.result_object({'error': f"{book}"}).get_response()



@api_view(['GET', 'PUT', "DELETE"])
@permission_classes([IsLoggedIn])
def book_detail(request, idx):
    response_builder = ResponseBuilder()
    book_service = BookService()
    try:
        book = book_service.get_book_by_idx(idx)
        reviews = ReviewService.get_reviews_by_book_idx(idx)
    except Exception as e:
        logger.error(f"BookDetailView get :: exception :: {e}")
        return response_builder.result_object({"error": f"{e}"}).fail().bad_request_400().get_response()
    
    if request.method in ["PUT", "DELETE"]:
        has_permissions = is_user_or_admin(request, idx)
        if not has_permissions:
            return response_builder.result_object({"error": "You don't have permissions to access this resource"}).get_response()

    if request.method=="GET":
        result = {
            'book': book,
            'reviews': reviews
        }
        return response_builder.get_200_success_response("Book details fetched successfully", result=result)

    
    if request.method == "PUT":
        book, is_error = book_service.update_book(book_idx=idx, new_data=request.data)
        if is_error:
            return response_builder.get_400_bad_request_response(error_code=-1, errors=book)
        return response_builder.get_200_success_response("Book Details updated successfullly", result=book)
    
    if request.method == 'DELETE':
        is_book_deleted = book_service.delete_book(book_idx=idx)
        if is_book_deleted:
            return response_builder.get_200_success_response("Book Deleted Successfully")
        return response_builder.result_object({'error': f"Couldn't Delete Book :: {e} "}).get_response()


@api_view(['GET'])
@permission_classes([IsLoggedIn])
def protected_view(request):
    response_builder = ResponseBuilder()
    return response_builder.result_object({"message": "This is protected View"}).get_response()