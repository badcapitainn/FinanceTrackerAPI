from .models import Account, Income, Expense, Savings
from .serializers import UserSerializer,AccountSerializer, IncomeSerializer, ExpenseSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

@csrf_exempt    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def create_bank_account(request):
    account_data = JSONParser().parse(request)
    account_serialiser = AccountSerializer(data = account_data)
    if account_serialiser.is_valid():
        account_serialiser.save(user = request.user)
        return Response({"message": "account saved"}, status= status.HTTP_201_CREATED)
    return Response(UserSerializer.errors, status= status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@api_view(['GET'])
def view_bank_accounts(request):
    account = Account.objects.filter(user = request.user)
    account_serializer = AccountSerializer(account, many = True)
    return Response(account_serializer.data, status= status.HTTP_302_FOUND)

@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@api_view(['PUT', 'PATCH'])
def update_accout_details(request, id):
    account_data = JSONParser().parse(request)
    try:
        account = Account.objects.get(id = id, user= request.user)
    except Account.DoesNotExist:
        return Response({'error':'task does not exist'}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        account_serializer = AccountSerializer(account, data = account_data)
    if request.method == 'PATCH':
        account_serializer = AccountSerializer(account, data= account_data, partial = True)
    
    if account_serializer.is_valid():
        account_serializer.save()
        return Response({'message':'account updated successfully'}, status= status.HTTP_200_OK)
    return Response({'error':'failed to update account'}, status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@api_view(['DELETE'])
def delete_account(request, id):
    try:
        account = Account.objects.get(id = id, user = request.user)
    except Account.DoesNotExist:
        return Response({'error':'account does not exist'})
    account.delete()
    return Response({'message':'account deleted'}, status = status.HTTP_200_OK)
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def add_income(request):
    income_data = JSONParser().parse(request)
    income_serializer = IncomeSerializer(data = income_data)
    if income_serializer.is_valid():
        income_serializer.save()
        return Response({'messege':'income added'}, status= status.HTTP_200_OK)
    return Response({'error':'failed to add income'})

