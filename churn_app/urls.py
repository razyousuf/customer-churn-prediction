# churn_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_page, name='home'),
    path('about/', views.about, name='about'),
    path('predict/', views.predict, name='predict'),
]
