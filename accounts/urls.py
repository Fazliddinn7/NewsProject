from django.urls import path
from .views import userLogin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', userLogin, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(
        template_name='registration/logged_out.html',
    ), name='logout'),
]
