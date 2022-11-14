from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# WRONG IMPORT: from django.views.generic.edit import CreateView
# CORRECT ONE:  from django.views.generic import CreateView

from petstagram.accounts.forms import PetstagramUserCreateForm
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginForm
# def login_user(request):
#     return render(request, 'accounts/login-page.html')


class UserRegisterView(CreateView):
    # model = PetstagramUser
    template_name = 'accounts/register-page.html'
    form_class = PetstagramUserCreateForm
    success_url = reverse_lazy('login')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
