from django.urls import path

from users.views import RegisterApi, LoginApi, LogoutApi


urlpatterns = [
    path('register', view=RegisterApi.as_view()),
    path('login', view=LoginApi.as_view()),
    path('logout', view=LogoutApi.as_view()),
]
