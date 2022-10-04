from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, delete_user, details_user, edit_user

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    # All profile actions - at one place, with include !!!!!
    path('profile/<int:pk>/', include([
        path('delete/', delete_user, name='delete user'),
        path('', details_user, name='details user'),
        path('edit', edit_user, name='edit user'),
    ]))
)
