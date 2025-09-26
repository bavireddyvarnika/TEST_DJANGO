# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(["GET"])
# def hello_world(request):
#     return Response({"Hello World"})

# ONLY GET
# from django.http import HttpResponse
# # from django.views.decorators.csrf import csrf_exempt
# # @csrf_exempt
# def hello_world(request):
#     print("...request=",request)
#     if request.method == "GET":
#         # manually return JSON string
#         return HttpResponse('{"message": "Hello World"}', content_type="application/json")
                            
#     else:
#         print("...1")
#         # if not GET, return 405
#         return HttpResponse("Method Not Allowed", status=405)
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

# Endpoint to get CSRF token (for Postman/JavaScript)
def csrf_token_view(request):
    return JsonResponse({"csrfToken": get_token(request)})

# POST endpoint that requires CSRF
def hello_world_post(request):
    if request.method == "POST":
        return HttpResponse(
            '{"message": "Hello World"}',
            content_type="application/json",
            status=201
        )
    return HttpResponse("Method Not Allowed", status=405)