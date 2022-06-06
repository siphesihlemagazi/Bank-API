from api.models import Account, Transaction
from api.serializers import AccountSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


@api_view(["GET", "POST"])
def account_list(request):
    if request.method == "GET":
        materials = Account.objects.all()
        serializer = AccountSerializer(materials, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def account_details(request, pk):
    try:
        account = Account.objects.get(pk=pk)

    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
