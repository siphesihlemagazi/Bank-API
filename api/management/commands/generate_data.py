from django.core.management import BaseCommand
from faker import Faker
import faker.providers
from django.contrib.auth.models import User
import random

from api.models import Account, Transaction

ACCOUNTS = ['Savings', 'Credit']
TRANSACTIONS = ['Deposit', 'Withdrawal']


class Provider(faker.providers.BaseProvider):
    def get_account_type(self):
        return self.random_element(ACCOUNTS)

    def get_transaction_type(self):
        return self.random_element(TRANSACTIONS)


class Command(BaseCommand):
    help = "Generate dummy data for testing"

    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(Provider)
        for _ in range(100):
            user = fake.name()
            User.objects.create_user(username=user.replace(' ', '').lower(), first_name=user.split()[0],
                                     last_name=user.split()[1], password='2020flex')

        for _ in range(100):
            acc_type = fake.get_account_type()
            holders = random.randint(User.objects.first().id, User.objects.last().id)

            Account.objects.create(
                holder=User.objects.filter(id=holders)[0], account_type=acc_type, balance=random.randint(50, 100000))

        for _ in range(100):
            trans = fake.get_transaction_type()
            accounts = random.randint(Account.objects.last().id, Account.objects.first().id)

            Transaction.objects.create(
                account=Account.objects.filter(id=accounts)[0], transaction_type=trans, amount=random.randint(50, 100000)
            )
