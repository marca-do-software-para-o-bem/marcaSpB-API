from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer
from .permission import UserPermission
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    # retorna o id do usuário ao mandar o nome de usuario
    @action(detail=False, methods=['get'])
    def get_user_by_username(self,request):
        user = User.objects.get(username=request.data['username'])
        return Response({"id": user.id})