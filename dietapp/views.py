from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import reverse_lazy
from dietapp.forms import DietImageUploadForm, DailyImageUploadForm
from dietapp.query import get_nutrition_charts, get_similar_diet
from dietapp.models import DailyDietImage
from profileapp.models import Profile

class DietUploadView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = DietImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            diet = form.save(commit=True)
            diet.fill_values(request.user)
            context = {'form':form, 'diet':diet}
            context['chart'] = get_nutrition_charts(diet.id)
            context['similar'] = get_similar_diet(diet.id)
            return render(request, 'dietapp/diet/main.html', context)

    def get(self, request: HttpRequest) -> HttpResponse:
        form = DietImageUploadForm()
        return render(request, 'dietapp/diet/main.html', {'form':form})


class DailyDietView(LoginRequiredMixin, View):
    login_url = reverse_lazy('accountapp:login')

    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            profile = Profile.objects.get(user=request.user)
        except :
            return redirect('accountapp:detail',pk=request.user.id)

        form = DailyImageUploadForm(request.POST, request.FILES)
        print(request.FILES)
        print('='*30)

        if form.is_valid():
            daily = form.save(uploader=request.user)
            daily.fill_values(request.user)
            context = {'form':form, 'daily':daily, 'profile':profile}

            return render(request, 'dietapp/daily/main.html', context)

    def get(self, request: HttpRequest) -> HttpResponse:
         try:
             profile = Profile.objects.get(user=request.user)
         except :
             return redirect('accountapp:detail',pk=request.user.id)
         
         return render(request, 'dietapp/daily/main.html', {'profile':profile})
    
    def update(request,pk):
        try:
            profile = Profile.objects.get(user=request.user)
        except :
            return redirect('accountapp:detail',pk=request.user.id)
            
        try:
            dailyDietImage = DailyDietImage.objects.get(pk)
        except :
            return redirect('diteapp:daily:main')
            
        if request.method == 'POST':
            form = DailyImageUploadForm(request.POST,instance=dailyDietImage) 
            if form.is_valid():
                form.save()
                context = {'form':form, 'daily':dailyDietImage, 'profile':profile}
                return render(request, 'dietapp/daily/main.html', context)
        else:
            form = DailyImageUploadForm(instance=dailyDietImage)
        return render(request,'update.html',{'form':form})

    def delete(request,pk):
        dailyDietImage = DailyDietImage.objects.get(pk=pk)
        dailyDietImage.delete() 
        return redirect('diteapp:daily:main')


    
        

