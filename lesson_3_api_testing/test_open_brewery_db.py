import pytest
import pprint
import random


class TestOpenBreweryTest:

    @pytest.mark.parametrize('number', [x for x in range(1, random.randint(10, 1000), random.randint(0, 100))])
    def test_get_random_single_brewery(self, number, open_brewery_db_client):
        path = f'/{number}'
        response = open_brewery_db_client.get_request(path=path)
        assert response.status_code == 200
        assert 'id' in response.json()
        assert 'name' in response.json()
        assert 'brewery_type' in response.json()
        assert 'street' in response.json()
        assert 'city' in response.json()
        assert 'state' in response.json()
        assert 'postal_code' in response.json()
        assert response.json()['id'] == number

    @pytest.mark.parametrize('cites, excepted_result',
                             [('san_diego', 'San Diego'), ('los_angeles', 'Los Angeles'), ('new_york', "New York"),
                              ('houston', 'Houston')])
    def test_by_city(self, open_brewery_db_client, cites, excepted_result):
        response = open_brewery_db_client.get_request(params={'by_city': cites})
        # print(response.url)
        # pprint.pprint(response.json())
        assert response.status_code == 200
        for item in range(len(response.json())):
            assert response.json()[item]['country'] == 'United States'
            assert response.json()[item]['city'] == excepted_result
