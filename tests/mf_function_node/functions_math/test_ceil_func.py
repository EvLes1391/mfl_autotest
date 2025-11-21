import pytest
import allure

@allure.title("Проверка функции CEIL")
def test_ceil_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('ceil(5.37)', '6')