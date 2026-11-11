import pytest

from part09_classes_object import BankAccount


@pytest.fixture
def account():
    return BankAccount("Ali", 1000)


def test_deposit(account):
    account.deposit(250)

    assert account.balance == 1250


def test_withdraw(account):
    account.withdraw(300)

    assert account.balance == 700


def test_transaction_history(account):
    account.deposit(250)
    account.withdraw(300)

    assert account.transaction_history == ["Deposited 250.00", "Withdrew 300.00"]


def test_deposit_rejects_negative_amount(account):
    with pytest.raises(ValueError, match="Deposit amount cannot be negative"):
        account.deposit(-1)


def test_withdraw_rejects_amount_over_balance(account):
    with pytest.raises(ValueError, match="Withdrawal exceeds available balance"):
        account.withdraw(1001)


def test_withdraw_rejects_negative_amount(account):
    with pytest.raises(ValueError, match="Withdrawal amount cannot be negative"):
        account.withdraw(-1)
