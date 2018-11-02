#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('<int:question_id>/', views.detail, name='detail'),
    url('<int:question_id>/results/', views.index, name='result'),
    url('<int:question_id>/vote/', views.index, name='vote'),
]