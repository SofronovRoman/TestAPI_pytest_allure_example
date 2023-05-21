import requests


class Methods:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, path='/', headers=None, params=None):
        url = f'{self.base_url}{path}'
        return requests.get(url=url, headers=self.headers, params=params)

    def post(self, path='/', headers=None, params=None):
        url = f'{self.base_url}{path}'
        return requests.post(url=url, headers=self.headers, params=params)

    def put(self, path='/', headers=None, params=None):
        url = f'{self.base_url}{path}'
        return requests.put(url=url, headers=self.headers, params=params)

    def delete(self, path='/', headers=None, params=None):
        url = f'{self.base_url}{path}'
        return requests.delete(url=url, headers=self.headers, params=params)
