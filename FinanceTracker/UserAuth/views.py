from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FinanceTrackerAPI.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


@csrf_exempt
@api_view(['POST'])
def registration(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data = user_data)
    if user_serializer.is_valid():
        user = user_serializer.save()
        token, created = Token.objects.get_or_create(user = user)
        return Response({'token': token.key, "user": user}, status= status.HTTP_200_OK)
    else:
       return Response({"error":"failed to create user"}, status= status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username = username, password = password)
    if user:
        token, created = Token.objects.get_or_create(user = user)
        return Response({'token': token.key, "user": username}, status= status.HTTP_200_OK)
    return Response({"error":"Wrong Credentials"}, status= status.HTTP_400_BAD_REQUEST)
    
    

@csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = Token.objects.get(user= request.user)
        token.delete()
        return Response({"message":"user successfully logged out"}, status=status.HTTP_200_OK)
    except token.DoesNotExist:
        return Response({'error':'token does not exist'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_auth(request):
    return Response(f"passed for {request.user.email}") 