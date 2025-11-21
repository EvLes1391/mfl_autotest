import pytest
import allure

@allure.title("Проверка функции TRUNC")
def test_trunc_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('trunc(7.99999)', '7')