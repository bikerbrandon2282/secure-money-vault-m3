from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage.as_view(), name='home'),
]