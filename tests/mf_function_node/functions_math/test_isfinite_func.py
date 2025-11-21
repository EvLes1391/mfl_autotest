import pytest
import allure

@allure.title("Проверка функции ISFINITE")
def test_isfinite_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('isfinite(387)', 'true')