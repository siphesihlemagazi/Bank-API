from django.urls import path
from api import views

urlpatterns = [
    path('accounts/', views.account_list),
    path('account/detail/<str:pk>/', views.account_details),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/detail/<str:pk>/', views.TransactionDetail.as_view()),
]