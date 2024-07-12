from .models import User, Account, Cartegory, Transaction, Budget, Goal, RecurringTransaction
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
    
class AccountSerializer(serializers.Serializer):
    class Meta:
        model = Account
        fields = '__all__'
        
class CartegorySerializer(serializers.Serializer):
    class Meta:
        model = Cartegory
        fields = '__all__'
        
class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
class BudgetSerializer(serializers.Serializer):
    class Meta:
        model = Budget
        fields = '__all__'
        
class GoalSerializer(serializers.Serializer):
    class Meta:
        model = Goal
        fields = '__all__'

class RecurringTransactionSerializer(serializers.Serializer):
    class Meta:
        model = RecurringTransaction
        fields = '__all__'