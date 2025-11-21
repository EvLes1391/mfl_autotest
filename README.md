readmemarkdown
## Для запуска:

- В `tests/pages/mf_function_page.py` в переменную `function_url` вставьте url потока на деве с названием `aut_func_flow`
- В `conftest.py` в функцию `def _login` в аргументы `username` и `password` запишите валидные значения
- **Запуск:** `pytest tests --headed --slowmo=1000` *(пока не понял как в конце при проверке assert'а задать нормальный wait, поэтому без slowmo тесты через раз валятся)*
- **Запуск с отчетами:** `pytest --alluredir=allure-results --headed --slowmo=1000`
- **Просмотр отчета:** `allure serve allure-results