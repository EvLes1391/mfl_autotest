import pytest
import allure

@allure.title("Проверка функции ABS")
def test_abs_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('abs(-5.7)', '5.7')