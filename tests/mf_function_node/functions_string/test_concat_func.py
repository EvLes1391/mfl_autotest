import pytest
import allure

@allure.title("Проверка функции CONCAT")
def test_concat_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('''concat("Этап", 'Hello')''', 'COLLECTING_MATERIALHello')