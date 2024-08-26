from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=500)
    balance = models.DecimalField(max_digits=100,decimal_places=2)
    account_currency = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Income(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=100,decimal_places= 2)
    currency = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    currency = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    goal = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

