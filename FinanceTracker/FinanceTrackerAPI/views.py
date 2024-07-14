from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Cartegory, Transaction, Budget, Goal, RecurringTransaction
from .serializers import UserRegistrationSerializer,UserLoginSerializer,AccountSerializer, CartegorySerializer, TransactionSerializer, BudgetSerializer, GoalSerializer, RecurringTransaction


@csrf_exempt
class Registration(generics.CreateAPIView):
    pass
    
@csrf_exempt
class Login(APIView):
    pass

@csrf_exempt
def accountAPI(request, id):
    pass