from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, AccountCreatioinForm
has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreatioinForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    login_url = reverse_lazy('accountapp:login')


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/update.html'
    login_url = reverse_lazy('accountapp:login')


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    login_url = reverse_lazy('accountapp:login')
