import pytest
import allure

@allure.title("Проверка функции SIGN")
def test_sign_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('sign(-45)', '-1')