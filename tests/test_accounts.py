import unittest

from etherscan.accounts import Account


SINGLE_BALANCE = '599582942930373018344492'
SINGLE_ACCOUNT = '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae'

MULTI_ACCOUNT = [
    '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
    '0x63a9975ba31b0b9626b34300f7f627147df1f526',
    '0x198ef1ec325a96cc354c7266a038be8b5c558f67'
]
MULTI_BALANCE = [
    {"account":"0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a","balance":"40891631566070000000000"},
    {"account":"0x63a9975ba31b0b9626b34300f7f627147df1f526","balance":"332567136222827062478"},
    {"account":"0x198ef1ec325a96cc354c7266a038be8b5c558f67","balance":"0"}
]
API_KEY = 'YourApiKeyToken'


class AccountsTestCase(unittest.TestCase):

    def test_get_balance(self):
        api = Account(address=SINGLE_ACCOUNT, api_key=API_KEY)
        self.assertEqual(api.get_balance(), SINGLE_BALANCE)

    def test_get_balance_multi(self):
        api = Account(address=MULTI_ACCOUNT, api_key=API_KEY)
        self.assertEqual(api.get_balance_multiple(), MULTI_BALANCE)
