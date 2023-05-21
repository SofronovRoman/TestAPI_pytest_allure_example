import pytest
import allure
from Config.TestData import TestData


@allure.feature('Тест метода DELETE')
class TestDelete:

    @allure.story('Удалить коллекцию')
    @pytest.mark.parametrize('id_collection', [TestData.ID_COLLECTION])
    def test_delete_collection(self, api, id_collection):
        response = api.delete(f'/collections/{id_collection}')
        with allure.step('Код ответа 204'):
            assert response.status_code == 204

    @allure.story('Удалить лайк фото')
    @pytest.mark.parametrize('id_photo', [TestData.ID_PHOTO])
    def test_delete_like_photo(self, api, id_photo):
        response = api.delete(f'/photos/{id_photo}/like')
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step('Значение ключа "id" содержится в ответе'):
            assert response_json['photo']['id'] == id_photo
