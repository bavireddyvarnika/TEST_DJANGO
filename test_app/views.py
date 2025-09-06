from django.shortcuts import render
from .forms import AdditionForm

def add_numbers(request):
    result = None
    form = AdditionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        result = a + b

    return render(request, "add.html", {"form": form, "result": result})