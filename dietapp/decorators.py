from django.shortcuts import render, redirect
from profileapp.models import Profile


def account_has_profile(func):
    def decorated(request, *args, **kwargs):
        try:
            Profile.objects.get(user=request.user)
        except:
            return redirect('accountapp:detail', pk=request.user.pk)
        return func(request, *args, **kwargs)
    return decorated


def account_has_profile_or_render(func):
    def decorated(request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
            return render(request, 'dietapp/daily/main.html',{'target_profile': profile})
        except:
            return redirect('accountapp:detail', pk=request.user.pk)
    return decorated
