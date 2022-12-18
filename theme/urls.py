from django.urls import path
from . import views

appname='theme.urls'

urlpatterns = [
    path('', views.index, name='index'),
]