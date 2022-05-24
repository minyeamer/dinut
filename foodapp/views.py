from django.shortcuts import render
from django.conf import settings
from foodapp.forms import FoodImageUploadForm


def upload_food_image(request):

    if request.method == 'POST':
        form = FoodImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return render(request, 'foodapp/upload.html', {'form':form,'food':food})
    else:
        form = FoodImageUploadForm()
        return render(request, 'foodapp/upload.html', {'form':form})
