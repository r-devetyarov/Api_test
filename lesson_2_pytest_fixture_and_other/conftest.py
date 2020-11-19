import pytest


@pytest.fixture(scope='function')
def create_list_7():
    new_list = [x for x in range(9999) if x % 7 == 0]
    print('\n Use function fixture')
    return new_list


@pytest.fixture(scope='module', params=[4, 8, 12, 16])
def create_first_number(request):
    print('\n Use module fixture')
    return request.param


@pytest.fixture
def create_sum(create_first_number):
    summa = create_first_number + 12
    return summa


@pytest.fixture
def create_dict(create_list_7, create_sum):
    new_dict = {'key_1': create_sum, 'key_2': create_list_7, 'key3': 'value'}
    print('\n User function fixture')
    return new_dict
