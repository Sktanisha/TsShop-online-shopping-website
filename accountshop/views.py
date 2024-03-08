from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')
def test(request):
    return render(request, 'test.html')
