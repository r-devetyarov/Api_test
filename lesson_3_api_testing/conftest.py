import pytest
import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, path=None, params=None, data=None, headers=None):
        if path is None:
            request_url = self.base_url
        else:
            request_url = self.base_url + path
        return requests.get(url=request_url, params=params, data=data, headers=headers)

    def post_request(self, path=None, data=None):
        if path is None:
            request_url = self.base_url
        else:
            request_url = self.base_url + path
        return requests.post(url=request_url, data=data)

    def put_request(self, path=None, data=None):
        if path is None:
            request_url = self.base_url
        else:
            request_url = self.base_url + path
        return requests.put(url=request_url, data=data)

    def delete_request(self, path=None, data=None):
        if path is None:
            request_url = self.base_url
        else:
            request_url = self.base_url + path
        return requests.delete(url=request_url, params=data)


@pytest.fixture
def dog_api_client():
    return APIClient(base_url='https://dog.ceo/api/')


@pytest.fixture
def open_brewery_db_client():
    return APIClient(base_url='https://api.openbrewerydb.org/breweries')


@pytest.fixture
def json_place_holder_client():
    return APIClient(base_url='https://jsonplaceholder.typicode.com/')


@pytest.fixture
def json_create_new_post(json_place_holder_client):
    data = {'title': 'TITLE: This post will be deleted',
            'body': 'TITLE: This post will be deleted',
            'userId': 1}
    response = json_place_holder_client.post_request(path='posts', data=data)
    if response.status_code == 201:
        return response
    else:
        raise print('Ошибка создания новго поста')


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="This is request URL")


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_get_url_params(url_param):
    return APIClient(base_url=url_param).get_request()
