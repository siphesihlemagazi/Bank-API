from api import views
from django.urls import path

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('account/detail/<str:pk>/', views.AccountDetail.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/detail/<str:pk>/', views.TransactionDetail.as_view()),
    path('register/', views.user_registration),
    path('user-account/', views.UserAccount.as_view()),
    path('user-account-detail/<str:pk>/', views.UserAccountDetail.as_view()),
    path('export-accounts/', views.export_accounts),
]
