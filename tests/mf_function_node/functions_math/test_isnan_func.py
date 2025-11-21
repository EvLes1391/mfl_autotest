import pytest
import allure

@allure.title("Проверка функции ISNAN")
def test_isnan_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('isnan(387)', 'false')