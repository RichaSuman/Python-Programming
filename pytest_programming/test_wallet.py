import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Return a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Return a Wallet instance with a balance of 20'''
    return Wallet(20)
    
def test_setting_initial_amount():
    w = Wallet(123)
    assert w.balance == 123

def test_wallet_add_cash():
    w = Wallet(10)
    w.add_cash(90)
    assert w.balance == 100

def test_wallet_spend_cash():
    w = Wallet(100)
    old_balance = w.balance
    w.spend_cash(40)
    assert w.balance == 60

def test_wallet_raise_exception_on_insufficient_amount():
    w = Wallet(50)
    with pytest.raises(InsufficientAmount):
        w.spend_cash(80)

        
@pytest.fixture
def my_wallet():
    '''Return a Wallet instance with a zero balance'''
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected",[
    (70,30,40),
    (100,50,50),
])

def test_transactions(earned,spent,expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected














