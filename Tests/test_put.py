import pytest
import allure
from Config.TestData import TestData

@allure.feature('Тест метода PUT')
class TestPut:

    @allure.story('Обновление коллекции')
    @pytest.mark.parametrize('id_collection', [TestData.ID_COLLECTION])
    def test_post_update_collection(self, api, id_collection):
        params = {'title': 'Cars', 'description': 'My photos of cars', 'private': 'false'}
        response = api.put(f'/collections/{id_collection}', params=params)
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step('Ответ содержит ключ "title" c установленным значением'):
            assert response_json['title'] == params['title']

    @allure.story('Обновление профиля пользователя')
    def test_post_update_collection(self, api):
        params = {'username': 'MIKE009', 'first_name': 'Mike', 'last_name': 'Joomla', 'location': 'Warsaw'}
        response = api.put(f'/me', params=params)
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step('Ответ содержит ключ "title" c установленным значением'):
            assert response_json['username'] == params['username'].lower()

