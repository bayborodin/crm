from django.test import TestCase

from accounts.models import AccountType


class AccountTypeTest(TestCase):

    def create_account_type(self, name='test account type', tsid='000-00-000-000'):
        return AccountType.objects.create(name=name, tsid=tsid)

    def test_account_type_creation(self):
        acc_type = self.create_account_type()
        self.assertTrue(isinstance(acc_type, AccountType))
        self.assertEqual(acc_type.__str__(), acc_type.name)
