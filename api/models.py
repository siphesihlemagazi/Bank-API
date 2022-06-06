from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

account_type = [('Savings', 'Savings'), ('Credit', 'Credit')]


class Account(models.Model):

    def clean(self):
        if self.type == 'Savings':
            if self.balance < 50:
                raise ValidationError("A savings account cannot have less than R50")

        if self.type == 'Credit':
            if self.balance < -20000:
                raise ValidationError("A credit account cannot have less than -R20000")

    holder = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=account_type)
    date_created = models.DateTimeField(default=datetime.now)
    balance = models.IntegerField()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.holder} - {self.balance}"


transaction_type = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=transaction_type)
    amount = models.IntegerField()
    date_created = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.type} - {self.date_created}"
