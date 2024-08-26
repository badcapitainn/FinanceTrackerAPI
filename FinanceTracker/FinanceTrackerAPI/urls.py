from . import views
from django.urls import path


urlpatterns = [
    path('createAccount/', views.create_bank_account),
    path('retrieveAccount', views.view_bank_accounts),
    path('updateAccount/<int:id>', views.update_accout_details),
    path('deleteAccount/<int:id>/delete/', views.delete_account)
]
