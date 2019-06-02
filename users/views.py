from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.permissions import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token


class RegisterApi(APIView):
    """
    注册
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self):
        pass

    def post(self, request):
        request_data = request.data

        username = request_data.get('username')
        password = request_data.get('password')
        print(username, password)

        queryset = User.objects.filter(username=username)

        if not queryset:
            User.objects.create_user(username=username, password=password)
            user = User.objects.get(username=username)
            token = Token.objects.create(user=user)
            data = {'msg': 'register success',
                    'data': {'token_id': token.key, 'user_id': token.user_id}}
            return Response(data=data, status=status.HTTP_201_CREATED)

        data = {'msg': 'register fail'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    """
    登录
    """
    def get(self, request):
        username = request.user.username
        print(username)
        data = {'msg': 'login success', 'data': username}
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data
        print(request_data)

        username = request_data.get('username')
        password = request_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user = User.objects.get(username=username)
            token = Token.objects.get(user_id=user.id)

            data = {'msg': 'login success',
                    'data': {'token_id': token.key}}
            return Response(data=data, status=status.HTTP_200_OK)

        data = {'msg': 'login fail'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class LogoutApi(APIView):
    """
    登出
    """
    def get(self, request):
        logout(request)
        data = {'msg': 'logout success'}
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self):
        pass
