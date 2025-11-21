import pytest
import allure

@allure.title("Проверка функции LEAST")
def test_least_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('least(5, 7, 1)', '1')