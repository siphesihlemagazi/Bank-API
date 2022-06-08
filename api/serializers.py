from rest_framework import serializers
from api.models import Account, Transaction
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class AccountSerializer(serializers.ModelSerializer):

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
            else:
                data['account'].deposit(data['amount'])
            return data

        if data['transaction_type'] == 'Withdrawal':
            if data['account'].account_type == 'Credit':
                if (data['account'].balance - data['amount']) < -20000:
                    raise ValidationError("You have insufficient funds")
                else:
                    data['account'].withdrawal(data['amount'])
                return data
            if data['account'].account_type == 'Savings':
                if (data['account'].balance - data['amount']) < 50:
                    raise ValidationError("You have insufficient funds")
                else:
                    data['account'].withdrawal(data['amount'])
                return data

    class Meta:
        model = Transaction
        fields = '__all__'
