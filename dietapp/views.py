from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from dietapp.forms import DietImageUploadForm
from dietapp.query import get_similar_diet


def diet_upload_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = DietImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            diet = form.save(commit=True)
            if not request.user.is_anonymous:
                diet.uploader = request.user
            diet.fill_values()
            return render(request, 'dietapp/diet.html', {'form':form,'diet':diet})
    else:
        form = DietImageUploadForm()
        return render(request, 'dietapp/diet.html', {'form':form})


def daily_diet_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'dietapp/daily_diet.html', {})
