from django.contrib import admin
from django.urls import include, path
import  users.vernemq 

urlpatterns = [
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]