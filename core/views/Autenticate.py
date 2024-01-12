from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from passlib.handlers.django import django_pbkdf2_sha256
from django.core.exceptions import ObjectDoesNotExist
from core.models import Usuario


@api_view(['POST'])
def login(request):
    checkUsuario = request.data['usuario']
    checkContrasenia = request.data['contrasenia']
    if user_exist(checkUsuario, checkContrasenia) == True:
        return Response({'message': 'Si existe'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Contraseña o correo invalidos'}, status=status.HTTP_400_BAD_REQUEST)


def user_exist(checkUsuario, checkContrasenia):
    try:
        usuarioSelecionado = Usuario.objects.get(correo=checkUsuario)
        if django_pbkdf2_sha256.verify(checkContrasenia, usuarioSelecionado.contrasenia):
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False
