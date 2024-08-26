from .models import Account,Income, Expense, Savings
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    account = serializers.PrimaryKeyRelatedField(many = True, queryset = Account.objects.all())
    
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password':{'write_only': True}}
    def create(self, data):
        user = User.objects.create_user(
            username= data['username'],
            email = data['email'],
            password = data['password']
        )
        return user

class AccountSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source = 'user.username')
    TYPE_CHOICES =[
        ('')
    ]
    
    class Meta:
        model = Account
        fields = '__all__'
        
        
class IncomeSerializer(serializers.ModelSerializer):
    TYPE_CHOICES =[('')]
    
    class Meta:
        model = Income
        fields = '__all__'
        
        
class ExpenseSerializer(serializers.ModelSerializer):
    TYPE_CHOICES= [('')]
    
    class Meta:
        model = Expense
        fields = '__all__'
        
        
class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = '__all__'