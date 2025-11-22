import pytest
import allure

@allure.title("Проверка функции LENGHT")
def test_concat_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('length("Этап")', '19')