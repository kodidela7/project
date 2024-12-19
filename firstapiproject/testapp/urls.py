from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.login_view, name='home'),  # This can be your login page or dashboard
    path('login/', views.login_view, name='login'),
    path('login_success/', views.login_success_view, name='login_success'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
