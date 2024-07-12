from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import User, Account, Cartegory, Transaction, Budget, Goal, RecurringTransaction
from .serializers import UserSerializer, AccountSerializer, CartegorySerializer, TransactionSerializer, BudgetSerializer, GoalSerializer, RecurringTransaction


@csrf_exempt
def userAPI(request, id):
    pass

def accountAPI(request, id):
    pass