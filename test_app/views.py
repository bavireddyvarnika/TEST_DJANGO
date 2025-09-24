# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(["GET"])
# def hello_world(request):
#     return Response({"Hello World"})
from django.http import HttpResponse

def hello_world(request):
    if request.method == "GET":
        # manually return JSON string
        return HttpResponse('{"message": "Hello World"}', content_type="application/json")
                            
    else:
        # if not GET, return 405
        return HttpResponse("Method Not Allowed", status=405)
