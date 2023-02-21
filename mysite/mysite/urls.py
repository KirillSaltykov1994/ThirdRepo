from django.contrib import admin
from django.urls import path, include
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),
    path('api/generate_credentials/', views.GenerateStaffs.as_view()),
 ]