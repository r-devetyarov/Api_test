import pytest
from random import randint


class TestJsonPlaceHolder:

    @pytest.mark.parametrize('count', [x for x in range(1, 100, randint(1, 15))])
    def test_get_posts_count(self, count, json_place_holder_client):
        path = f'posts/{count}'
        response = json_place_holder_client.get_request(path=path)
        print(response.url)
        assert response.status_code == 200
        assert response.json()['id'] == count

    @pytest.mark.parametrize('count', [x for x in range(1, 100, randint(1, 15))])
    def test_put_posts_create(self, count, json_place_holder_client):
        path = 'posts'
        data = {
            'title': f'New title number {count}',
            'body': f'New body number {count}',
            'userId': 1
        }

        response = json_place_holder_client.post_request(path=path, data=data)
        assert response.status_code == 201
        assert response.json()['title'] == data['title']
        assert response.json()['body'] == data['body']
        assert int(response.json()['userId']) == 1

    def test_delete_post(self, json_create_new_post, json_place_holder_client):
        id_post = str(json_create_new_post.json()["id"])
        path = f'posts/{id_post}'
        response = json_place_holder_client.delete_request(path=path)
        assert response.status_code == 200
        response = json_place_holder_client.get_request(path=path)
        assert response.status_code == 404

    def test_edit_post_method_put(self, json_place_holder_client):
        path = 'posts/1'
        data = {'id': 1,
                'title': 'New title after edit',
                'body': 'New body after edit',
                'userId': 1}
        response = json_place_holder_client.put_request(path=path, data=data)
        assert response.status_code == 200
        assert response.json()['title'] == data['title']
        assert response.json()['body'] == data['body']
