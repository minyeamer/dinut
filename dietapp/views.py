from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from dietapp.forms import DietImageUploadForm


def diet_upload_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = DietImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            diet = form.save(commit=True)
            if request.user:
                diet.uploader = request.user
            diet.analyze_diet(settings.MEDIA_ROOT_URL + diet.upload_diet.url)
            diet.save()
            return render(request, 'dietapp/diet.html', {'form':form,'diet':diet})
    else:
        form = DietImageUploadForm()
        return render(request, 'dietapp/diet.html', {'form':form})


def daily_diet_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'dietapp/daily_diet.html', {})
