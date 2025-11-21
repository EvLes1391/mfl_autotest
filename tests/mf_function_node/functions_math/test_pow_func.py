import pytest
import allure

@allure.title("Проверка функции POW")
def test_pow_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('pow(3, 2)', '9')