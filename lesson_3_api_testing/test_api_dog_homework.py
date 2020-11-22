import pytest
import pprint


class TestApiDog:

    def test_get_list_all_breeds(self, dog_api_client, path='breeds/list/all'):
        response = dog_api_client.get_request(path=path)
        # pprint.pprint(response.json())
        assert response.status_code == 200
        assert 'message' in response.json()
        assert response.json()['status'] == 'success'

    def test_get_random_image(self, dog_api_client, path='breeds/image/random'):
        response = dog_api_client.get_request(path=path)
        assert response.status_code == 200
        assert 'message' in response.json()
        assert 'status' in response.json()
        assert response.json()['status'] == 'success'

    @pytest.mark.parametrize('valid_count', [x for x in range(1, 50, 1)])
    def test_get_random_image_count(self, dog_api_client, valid_count):
        path = f'breeds/image/random/{valid_count}'
        response = dog_api_client.get_request(path=path)
        assert response.status_code == 200
        assert 'message' in response.json()
        assert 'status' in response.json()
        assert response.json()['status'] == 'success'
        assert len(response.json()['message']) == valid_count

