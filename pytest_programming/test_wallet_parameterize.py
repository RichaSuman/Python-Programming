import pytest
from wallet import Wallet

        
@pytest.fixture
def my_wallet():
    '''Return a Wallet instance with a zero balance'''
    return Wallet()


@pytest.mark.parametrize("earned,spent,expected",[
    (70,30,40),
    (100,50,60),
])

def test_transactions(earned,spent,expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected














