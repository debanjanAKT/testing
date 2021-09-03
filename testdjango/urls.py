
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('lokesh.urls')),
    path('admin/', admin.site.urls),
   
]
