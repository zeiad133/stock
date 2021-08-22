from django.urls import include, path
import  app.services.vernemq 

urlpatterns = [
    path('api/', include('app.urls'))
]