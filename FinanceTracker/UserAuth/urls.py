from . import views
from django.urls import path

urlpatterns = [
    path('registration/', views.registration),
    path('login/', views.login),
    path('logout/', views.logout),
    path('test/', views.test_auth)
]
