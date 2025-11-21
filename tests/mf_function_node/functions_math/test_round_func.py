import pytest
import allure

@allure.title("Проверка функции ROUND")
def test_round_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('round(3.14159, 3)', '3.142')