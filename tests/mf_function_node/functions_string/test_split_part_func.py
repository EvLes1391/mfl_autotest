import pytest
import allure

@allure.title("Проверка функции  SPLIT_PART")
def test_concat_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test("split_part('Маша/Саша/Паша', '/', 2)", 'Саша')