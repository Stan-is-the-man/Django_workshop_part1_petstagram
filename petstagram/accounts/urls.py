from django.urls import path, include

from petstagram.accounts.views import login_user, delete_user, details_user, edit_user, UserRegisterView

urlpatterns = (
    path('login/', login_user, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # All profile actions - at one place, with include !!!!!
    path('profile/<int:pk>/', include([
        path('delete/', delete_user, name='delete user'),
        path('', details_user, name='details user'),
        path('edit/', edit_user, name='edit user'),
    ]))
)
