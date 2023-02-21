from django.contrib import admin
from django.urls import path, include
from myapi2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi2.urls')),
    path('api/generate_credentials/', views.GenerateStaffs.as_view()),
 ]