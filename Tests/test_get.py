import pytest
import allure
from Config.TestData import TestData

@allure.feature('Тест метода GET')
class TestGet:

    @pytest.mark.parametrize('username', [TestData.USERNAME])
    @allure.story('Получить общедоступный профиль пользователя')
    def test_get_username_profile(self, api, username):
        response = api.get(f'/users/{username}')
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step('Ответ содержит ключ "username" с запрашиваемым значением'):
            assert response_json['username'] == username

    @allure.story('Получить ссылку на портфолио пользователя')
    @pytest.mark.parametrize('username', [TestData.USERNAME])
    def test_get_user_portfolio_link(self, api, username):
        response = api.get(f'/users/{username}/portfolio')
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step('Ответ содержит ключ "url"'):
            assert 'url' in response_json

    @allure.story('Получить случайное фото')
    def test_get_random_photo(self, api):
        params = {'count': TestData.COUNT}
        response = api.get(f'/photos/random', params=params)
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step(f'Ответ содержит запрашиваемое количество объектов'):
            assert len(response_json) == params['count']

    @allure.story('Получить статистику фотографии')
    @pytest.mark.parametrize('id_photo', [TestData.ID_PHOTO])
    def test_get_photo_statistics(self, api, id_photo):
        response = api.get(f'/photos/{id_photo}/statistics')
        response_json = response.json()
        with allure.step('Код ответа 200'):
            assert response.status_code == 200
        with allure.step('Ответ содержит ключ "id"'):
            assert response_json['id'] == id_photo

