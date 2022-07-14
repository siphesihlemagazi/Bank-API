import csv
from api.models import Account, Transaction
from api.serializers import AccountSerializer, TransactionSerializer, UserSerializer
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class AccountList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        user_id = self.request.GET.get('user_id')

        if user_id:
            queryset = queryset.filter(holder__id=user_id)

        return queryset


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        user_id = self.request.GET.get('user_id')

        if user_id:
            queryset = queryset.filter(holder__id=user_id)

        return queryset


class TransactionList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        user_id = self.request.GET.get('user_id')

        if user_id:
            queryset = queryset.filter(holder__id=user_id)

        return queryset


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        user_id = self.request.GET.get('user_id')

        if user_id:
            queryset = queryset.filter(holder__id=user_id)

        return queryset


@api_view(["POST"])
def user_registration(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAccount(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer()

    def list(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(holder=request.user)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)


class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer()

    def get(self, request, pk):
        queryset = self.get_queryset()
        queryset = queryset.filter(holder=request.user)
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)


def export_accounts(request):
    if request.user.is_staff:
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['Acc Holder', 'Acc Type', 'Available Balance', 'Date Created'])

        for account in Account.objects.all().values_list('holder', 'account_type', 'balance', 'date_created'):
            writer.writerow(account)

        response['Content-Disposition'] = 'attachment; filename="accounts.csv"'

        return response
    else:
        return HttpResponse('Access Denied')

