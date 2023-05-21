<strong>Репозиторий содержит пример скриптов тестирования API сервиса UNSPLASH (https://unsplash.com/documentation). Используются модули requests, pytest и allure. 
 Аналогичный функционал реализован в POSTMAN, коллекции и глобальные переменные находятся в папке "Postman". Представленный материал является учебным
 пособием.</strong>
 
 ## Установка
```ruby
$ git clone https://github.com/SofronovRoman/TestAPI_pytest_allure_example.git
$ cd TestAPI_pytest_allure_example
$ pip install -r requirements.txt
```
## Настройка
Тестовые данные находятся в Config\TestData.py, при необходимости можно изменять существующие или добавлять новые данные.

## Использование
```ruby
$ pytest --alluredir=allure_report
$ allure serve allure_report
```

## Источники
Документация [Allure](https://docs.qameta.io/allure-report/#_pytest)  
Документация [Pytest](https://docs.pytest.org/en/latest/contents.html#)  
Документация [Requests](https://requests.readthedocs.io/en/latest/)
