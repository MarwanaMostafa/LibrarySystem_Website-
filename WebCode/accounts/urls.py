from django.urls import path
from django.urls.resolvers import URLPattern
from . import views as acc_views
from django.contrib.auth import views



urlpatterns = [
    path('signup/', acc_views.signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name = 'pages/LogIn_SignUp.html'), name='login'),
    path('profile/', acc_views.profile, name='profile'),
    path('edit/', acc_views.editprofile, name='editprofile'),
    path('logout/', views.LogoutView.as_view(template_name = 'pages/logout.html'), name='logout'),
]