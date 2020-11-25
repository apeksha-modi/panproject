from django.contrib import admin
from django.urls import path , include
from gallery import views


urlpatterns = [
    path('', views.index,name='index'),
    path('upload',views.uploadImage, name = 'uploadImage')

]
