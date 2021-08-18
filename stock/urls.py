from django.contrib import admin
from django.urls import include, path
# import  users.vernemq 
from rest_framework import routers, serializers, viewsets
from users.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'wallet']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('app.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]