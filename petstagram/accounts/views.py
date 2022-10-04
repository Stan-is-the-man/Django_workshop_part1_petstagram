from django.shortcuts import render


def login_user(request):
    return render(request, 'accounts/login-page.html')


def register_user(request):
    return render(request, 'accounts/register-page.html')


# adding extra variable pk, so the url can be displayed for testing
def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
