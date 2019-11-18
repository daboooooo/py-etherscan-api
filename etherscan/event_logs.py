from .client import Client


class EventLogs(Client):
    def __init__(self, address=Client.dao_address, api_key='YourApiKeyToken'):
        Client.__init__(self, address=address, api_key=api_key)
        self.url_dict[self.MODULE] = 'logs'

    def get_event_logs(self, from_block='0', to_block='latest', topic0=''):
        self.url_dict[self.ACTION] = 'getLogs'
        self.url_dict[self.FROM_BLOCK] = from_block
        self.url_dict[self.TO_BLOCK] = to_block
        self.url_dict[self.TOPIC0] = topic0

        self.build_url()
        req = self.connect()
        return req['result']
