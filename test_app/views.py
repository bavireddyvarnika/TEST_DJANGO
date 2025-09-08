from django.http import JsonResponse
from django.shortcuts import render

def add_page(request):
    # Renders the page with inputs (no Django form)
    return render(request, "add.html")

def add_numbers_api(request):
    print("request:",request)
    # API endpoint that returns JSON (no HTML form)
    try:
        a = int(request.GET.get("a", ""))
        b = int(request.GET.get("b", ""))
    except ValueError:
        return JsonResponse({"ok": False, "error": "Please provide valid integers for a and b."}, status=400)

    return JsonResponse({"ok": True, "a": a, "b": b, "result": a + b})