from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=500)
    account_type = models.CharField(max_length=500) #  bank | credit | cash
    balance = models.DecimalField(max_digits=100,decimal_places=2)
    account_currency = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Cartegory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    cartegory_type = models.CharField(max_length = 50) # income | Expence

class  Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    cartegory = models.ForeignKey(Cartegory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    transaction_type = models.CharField(max_length=50) # Income | Expence
    description = models.CharField(max_length=1000)
    date = models.DateField()
    recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    cartegory = models.ForeignKey(Cartegory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    target_amount = models.DecimalField(max_digits=100,decimal_places=2)
    current_amount = models.DecimalField(max_digits=100,decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    
class RecurringTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    cartegory = models.ForeignKey(Cartegory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100,decimal_places= 2)
    transcation_type = models.CharField(max_length=50) #income | expence
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    frequency = models.CharField(max_length=50) # weekly | monthly
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    


