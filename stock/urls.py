from django.contrib import admin
from django.urls import include, path
import  polls.vernemq 

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]