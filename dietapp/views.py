from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from dietapp.forms import DietImageUploadForm, DailyImageUploadForm
from dietapp.query import get_nutrition_charts, get_similar_diet
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
        profile = get_object_or_404(Profile, user=request.user)
        form = DailyImageUploadForm(request.POST, request.FILES)
        print(request.FILES)
        print('='*30)
        if form.is_valid():
            daily = form.save(commit=True)
            daily.fill_values(request.user)
            context = {'form':form, 'daily':daily, 'profile':profile}
            return render(request, 'dietapp/daily/main.html', context)

    def get(self, request: HttpRequest) -> HttpResponse:
        profile = get_object_or_404(Profile, user=request.user)
        form = DailyImageUploadForm()
        return render(request, 'dietapp/daily/main.html', {'profile':profile})
