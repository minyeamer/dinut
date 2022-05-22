from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def temp_upload(request: HttpRequest):
    return render(request, 'foodapp/upload.html')
