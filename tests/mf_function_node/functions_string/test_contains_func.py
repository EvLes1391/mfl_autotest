import pytest
import allure

@allure.title("Проверка функции  CONTAINS")
def test_concat_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('''contains("Этап", 'THINKING')''', "true")