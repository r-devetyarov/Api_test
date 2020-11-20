import pytest
import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, path, params=None, data=None, headers=None):
        request_url = self.base_url + path
        return requests.get(url=request_url, params=params, data=data, headers=headers)

    def post_request(self, path, params=None):
        request_url = self.base_url + path
        return requests.post(url=request_url, params=params)


@pytest.fixture
def dog_api_client():
    return APIClient(base_url='https://dog.ceo/api/')
