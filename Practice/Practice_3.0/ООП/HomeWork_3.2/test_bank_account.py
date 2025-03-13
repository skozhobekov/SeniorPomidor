import pytest
from BankAccount import BankAccount


def test_if_sum_more_than_0():
    sa = BankAccount("Sanjar")
    sa.deposit(1000)
    sa.withdraw(200)
    result = sa.get_balance()
    assert result > 0