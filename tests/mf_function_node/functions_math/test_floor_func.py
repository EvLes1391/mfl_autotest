import pytest
import allure

@allure.title("Проверка функции FLOOR")
def test_floor_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('floor(5.9)', '5')