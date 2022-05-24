from .forms import ImageUploadForm 
from django.shortcuts import render
from django.conf import settings 


def temp_upload(request): 

    if request.method == 'POST' : 
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)  
            post.save() 
            
            imageURL = settings.MEDIA_URL + form.instance.foodImage.name 

            return render(request, 'foodapp/upload.html', {'form':form, 'post':post}) 

    else: 
         form = ImageUploadForm() 
         return render(request, 'foodapp/upload.html', {'form':form}) 