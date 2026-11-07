# Проверка страницы товара

Задание 3.6.10 курса https://stepik.org/course/575.

Установка и запуск:

```sh
pip install -r requirements.txt
pytest --language=es test_items.py
pytest --language=fr test_items.py
```

Тест открывает страницу товара и проверяет, что на ней есть ровно одна кнопка добавления в корзину.
Браузер создаётся в фикстуре и закрывается после теста.

Для локального Chrome for Testing можно задать `CHROME_BINARY` и `SE_CHROMEDRIVER`.
`HEADLESS=1` запускает тест без видимого окна. По умолчанию используется обычный Chrome.
