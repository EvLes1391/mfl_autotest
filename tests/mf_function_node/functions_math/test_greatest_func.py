import pytest
import allure

@allure.title("Проверка функции GREATEST")
def test_greatest_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('greatest(5, 7, 1)', '7')