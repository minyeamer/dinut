from distutils.command.upload import upload
import profile
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from dietapp.forms import DietImageUploadForm, DailyImageUploadForm
from dietapp.query import get_nutrition_charts, get_similar_diet, get_date_fommater
from dietapp.models import DailyDietImage
from profileapp.models import Profile
from django.contrib import messages

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
    profile_url = reverse_lazy('accountapp:detail')
    daily_main_url = reverse_lazy('dietapp:daily')

    def index(request):
         cur_user = request.user
         if not cur_user.is_authenticated:
            return redirect(DailyDietView.login_url)
         try:
             profile = Profile.objects.get(user=request.user)
         except :
            return redirect(DailyDietView.profile_url, pk=request.user.id)
         
         return render(request, 'dietapp/daily/main.html',{'profile': profile})
    
    def detail(request):
        if request.method == 'POST': 
            form = DailyImageUploadForm(request.POST, request.FILES)
            
            if form.is_valid():
                daily = form.save(uploader=request.user)
                daily.fill_values(request.user)
                target_date = form.cleaned_data['target_date']
                date_list = {'year': target_date.year, 'month': target_date.month, 'day': target_date.day, 'target_date': target_date}
                context = {'form':form, 'daily':daily, 'date_list': date_list}
                messages.info(request, '식단이 정상적으로 등록되었습니다.')
                return render(request, 'dietapp/daily/detail.html', context)

            else:
                messages.info(request, '일시적인 서버오류로 식단 등록에 실패하였습니다.')
                return render(request, 'dietapp/daily/detail.html')

        else :
                target_date  = request.GET.get('target_date')
                date_list = get_date_fommater(target_date)

                try :
                    dailyDietImage = DailyDietImage.objects.get(uploader=request.user, target_date=target_date)
                except :
                    return render(request, 'dietapp/daily/detail.html',{'date_list':date_list })

                context = {'daily': dailyDietImage, 'date_list': date_list}
                return render(request, 'dietapp/daily/detail.html', context)
    

    def update(request):
        target_date  = request.GET.get('target_date')
        date_list = get_date_fommater(target_date)
        print('update_date=',target_date)

        try :
            dailyDietImage = DailyDietImage.objects.get(uploader=request.user, target_date=target_date)
        except :
            messages.info(request, '일시적인 서버 오류로 식단 변경에 실패하였습니다.')
            return redirect(DailyDietView.daily_main_url)

        context = {'daily': dailyDietImage, 'date_list':date_list}

        if request.method == 'POST':
            form = DailyImageUploadForm(request.POST, request.FILES,instance=dailyDietImage)
            print("=============",request.FILES)
            if form.is_valid():
                form.save(uploader=request.user)
                messages.info(request, '식단이 정상적으로 변경되었습니다.')
                render(request,'dietapp/daily/detail.html', context);   

        form = DailyImageUploadForm(instance=dailyDietImage)
        return render(request,'dietapp/daily/update.html', context)       

    def delete(request):
        target_date  = request.GET.get('target_date')
        try :
            dailyDietImage = DailyDietImage.objects.get(uploader=request.user, target_date=target_date)
        except :
            messages.info(request, '일시적인 서버 오류로 식단 삭제에 실패하였습니다.')
            return redirect(DailyDietView.daily_main_url)
        dailyDietImage.delete() 
        messages.info(request, '식단이 정상적으로 전부 삭제되었습니다.')
        return redirect(DailyDietView.daily_main_url)

