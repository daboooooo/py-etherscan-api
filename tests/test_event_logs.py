import unittest

from etherscan.event_logs import EventLogs

FROM_BLOCK = '379224'
TO_BLOCK = '379300'
ADDRESS = '0x33990122638b9132ca29c723bdf037f1a891a70c'
TOPIC0 = '0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545'
API_KEY = 'YourApiKeyToken'

EVENT_LOGS = [
    {"address":"0x33990122638b9132ca29c723bdf037f1a891a70c","topics":["0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545","0x72657075746174696f6e00000000000000000000000000000000000000000000","0x000000000000000000000000d9b2f59f3b5c7b3c67047d2f03c3e8052470be92"],"data":"0x","blockNumber":"0x5c958","timeStamp":"0x561d688c","gasPrice":"0xba43b7400","gasUsed":"0x10682","logIndex":"0x","transactionHash":"0x0b03498648ae2da924f961dda00dc6bb0a8df15519262b7e012b7d67f4bb7e83","transactionIndex":"0x"},
    {"address":"0x33990122638b9132ca29c723bdf037f1a891a70c","topics":["0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545","0x6c6f747465727900000000000000000000000000000000000000000000000000","0x0000000000000000000000001f6cc3f7c927e1196c03ac49c5aff0d39c9d103d"],"data":"0x","blockNumber":"0x5c965","timeStamp":"0x561d6930","gasPrice":"0xba43b7400","gasUsed":"0x105c2","logIndex":"0x","transactionHash":"0x8c72ea19b48947c4339077bd9c9c09a780dfbdb1cafe68db4d29cdf2754adc11","transactionIndex":"0x"}
]

class TokensTestCase(unittest.TestCase):

    def test_get_token_supply(self):
        api = EventLogs(address=ADDRESS, api_key=(API_KEY))
        event_result = api.get_event_logs(from_block=FROM_BLOCK,to_block=TO_BLOCK,topic0=TOPIC0)
        self.assertEqual(event_result, EVENT_LOGS)

if __name__ == '__main__':
    unittest.main()
