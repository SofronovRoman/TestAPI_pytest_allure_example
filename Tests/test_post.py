import pytest
import allure
from Config.TestData import TestData


@allure.feature('Тест метода POST')
class TestPost:

    @allure.story('Создание коллекции')
    def test_post_create_collection(self, api):
        params = {'title': 'Forest', 'description': 'My photos of forests', 'private': 'false'}
        response = api.post(f'/collections', params=params)
        response_json = response.json()
        with allure.step('Код ответа 201'):
            assert response.status_code == 201
        with allure.step('Ответ содержит ключ "title" c установленным значением'):
            assert response_json['title'] == params['title']

    @allure.story('Добавить фото в коллекцию')
    @pytest.mark.parametrize('id_collection', [TestData.ID_COLLECTION])
    @pytest.mark.parametrize('photo_id', [TestData.ID_PHOTO])
    def test_post_add_photo_to_collection(self, api, id_collection, photo_id):
        params = {'photo_id': photo_id}
        response = api.post(f'/collections/{id_collection}/add', params=params)
        response_json = response.json()
        with allure.step('Код ответа 201'):
            assert response.status_code == 201
        with allure.step('Значение ключа "id" содержится в ответе'):
            assert response_json['photo']['id'] == photo_id

    @allure.story('Лайк фото')
    @pytest.mark.parametrize('photo_id', [TestData.ID_PHOTO])
    def test_post_add_photo_to_collection(self, api, photo_id):
        response = api.post(f'/photos/{photo_id}/like')
        response_json = response.json()
        with allure.step('Код ответа 201'):
            assert response.status_code == 201
        with allure.step('id фото содержится в коллекции'):
            assert response_json['photo']['id'] == photo_id

