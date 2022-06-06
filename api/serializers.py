from rest_framework import serializers
from api.models import Account, Transaction
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class AccountSerializer(serializers.ModelSerializer):
    holder = UserSerializer(read_only=True)

    def validate(self, data):
        if data['account_type'] == 'Savings':
            if data['balance'] < 50:
                raise ValidationError("A savings account cannot have less than R50")
            return data

        if data['account_type'] == 'Credit':
            if data['balance'] < -20000:
                raise ValidationError("A credit account cannot have less than -R20000")
            return data

    class Meta:
        model = Account
        fields = ['id', 'holder', 'account_type', 'balance', 'date_created']


class TransactionSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['transaction_type'] == 'Deposit':
            if data['amount'] < 0.1:
                raise ValidationError("Deposit start at 0.1 cent")
            return data

        if data['transaction_type'] == 'Withdrawal':
            if data['amount'] > data['account.balance']:
                raise ValidationError("You have insufficient funds")
            return data

    class Meta:
        model = Transaction
        fields = '__all__'
