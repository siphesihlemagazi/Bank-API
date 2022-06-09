from django.urls import path
from api import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('account/detail/<str:pk>/', views.AccountDetail.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/detail/<str:pk>/', views.TransactionDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/detail/<str:pk>/', views.UserDetail.as_view()),
    path('register/', views.user_registration),
]
