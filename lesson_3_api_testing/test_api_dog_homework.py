import pytest
import pprint


class TestApiDog:

    def test_get_list_all_breeds(self, dog_api_client, path='breeds/list/all'):
        response = dog_api_client.get_request(path=path)
        # pprint.pprint(response.json())
        assert response.status_code == 200
        assert 'message' in response.json()
        assert response.json()['status'] == 'success'