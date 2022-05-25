from django.shortcuts import render
from django.conf import settings
from foodapp.forms import FoodImageUploadForm
from foodapp.analyze import analyze_diet


def upload_food_image(request):
    if request.method == 'POST':
        form = FoodImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            if request.user:
                food.uploader = request.user
            food.save()
            result = analyze_diet(settings.MEDIA_ROOT_URL + food.food_image.url)
            return render(request, 'foodapp/analysis.html', {'form':form,'food':food,'result':result})
    else:
        form = FoodImageUploadForm()
        return render(request, 'foodapp/analysis.html', {'form':form})
