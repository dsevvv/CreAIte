import json
import re


class PrintifyClient:
    def __init__(self, client, access_token):
        self.client = client
        self.access_token = access_token

    def request(self, method, uri='', data=None):
        if data is None:
            data = []
        options = {'headers': {'Authorization': f'Bearer {self.access_token}'}}
        if data:
            options['json'] = data
        response = self.client.request(method, uri, **options)
        return json.loads(response.text)

    def request_product_list(self, method, uri='', data=None):
        if data is None:
            data = []
        options = {'headers': {'Authorization': f'Bearer {self.access_token}'}}
        if data:
            options['json'] = data
        response = self.client.request(method, uri, **options)
        product_ids = re.findall(r'[a-fA-F0-9]{24}', response.text)
        return product_ids



