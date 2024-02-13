from django.shortcuts import render
import random
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import re


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in
                   range(length))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'erro': 'Envie um request com parâmetros válidos'})

    username = request.POST['email']
    password = request.POST['password']

    if not re.match(
            "/[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/",
            username):
        return JsonResponse({"erro": "Coloque um email válido"})

    if len(password) < 3:
        return JsonResponse({"erro": "Coloque uma senha válida, com mais de 3 caracteres"})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({"erro": "Usuário não deslogado"})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({"token": token, 'user': usr_dict})
        else:
            return JsonResponse({"erro": "Senha inválida"})

    except UserModel.DoesNotExist:
        return JsonResponse({"erro": "Email inválido"})


def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'erro': 'ID de usuário inválido'})

    return JsonResponse({'successo': 'Logout feito com sucesso'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny], 'list': [IsAdminUser]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]


#Isso aqui garante que ninguém vai conseguir criar um super user acessando a rota!!!
    def perform_create(self, serializer):
        # Garante que is_staff e is_superuser sejam sempre False ao criar um usuário
        serializer.validated_data['is_staff'] = False
        serializer.validated_data['is_superuser'] = False
        serializer.save()