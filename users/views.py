from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserRegisterForm
from users.serializers import UserSerializer, UserLoginSerializer


@api_view(['Post'])
def register(request):
    if request.user.is_authenticated():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.user.is_authenticated:
    #     return redirect('home')
    #
    # # if request.method == 'POST':
    # #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}! You are able to login!')
    #         return redirect('login')
    # else:
    #     form = UserRegisterForm()
    # return render(request, 'users/register.html', {'form': form})

class Login(APIView):
    def post(self, request):
        if request.user.is_authenticated():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={"error":"Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        return Response(status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)
