class Account:

    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        else:
            self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account: 'Account', amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        yield self._transactions

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __it__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc = Account(owner = f"{self.owner}&{other.owner}", amount = self.amount + other.amount)
        acc._transactions.extend(self._transactions + other._transactions)
        return acc


#
# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)


import unittest
import types

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Stefan", 50)
        self.account_other = Account("Ivan", 100)

    def test_validation_tr(self):
        res = Account.validate_transaction(self.account, 50)
        self.assertEqual(res, "New balance: 100")

    def test_validate_tr_invalid(self):
        with self.assertRaises(ValueError) as ex:
            res = Account.validate_transaction(self.account, -51)

    def test_str(self):
        self.assertEqual(str(self.account), "Account of Stefan with starting amount: 50")

    def test_repr(self):
        self.assertEqual(repr(self.account), "Account(Stefan, 50)")

    def test_add_transaction(self):
        self.assertEqual(len(self.account._transactions), 0)
        self.account.add_transaction(20)
        self.assertEqual(len(self.account._transactions), 1)
        self.assertEqual(self.account.balance, 70)

    def test_add_transaction_invalid_type(self):
        with self.assertRaises(ValueError) as ex:
            self.account.add_transaction(5.6)

    def test_get_item(self):
        self.account.add_transaction(20)
        self.assertEqual(self.account[0], 20)

    def test_raise_error_index(self):
        with self.assertRaises(IndexError) as ex:
            self.assertEqual(self.account[0], 20)

    def test_reversce(self):
        self.account.add_transaction(50)
        self.account.add_transaction(100)
        self.assertEqual(list(reversed(self.account)), [100, 50])

    def test_are_not_equal(self):
        self.assertNotEqual(self.account, self.account_other)

    def test_less_than(self):
        self.assertLess(self.account, self.account_other)

    def test_greater_than(self):
        self.assertGreater(self.account_other, self.account)
        self.assertTrue(self.account_other > self.account)

    def test_add(self):
        res = self.account + self.account_other
        self.assertEqual(res.balance, 150)

    def test_len_account(self):
        self.account.add_transaction(20)
        self.account.add_transaction(50)
        self.assertEqual(len(self.account), 2)

    def test_g_e(self):
        ac3 = Account("Other", 50)
        self.assertEqual(self.account, ac3)

    def test_if_validate_is_static(self):
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_greater_or_equal(self):
        ac3 = Account("Other", 50)
        self.assertGreaterEqual(ac3, self.account)

if __name__ == "__main__":
    unittest.main()