from django.urls import include, path
from rest_framework import routers
from usuario import views

router = routers.DefaultRouter()
router.register(r'usuario', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]