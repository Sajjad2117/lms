from . import views

from .views import IndexView, DetailView, register_form_view
from django.urls import path

app_name = 'education'

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('register-form/', register_form_view, name='register-form'),

]


