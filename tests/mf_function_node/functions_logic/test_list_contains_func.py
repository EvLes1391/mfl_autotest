import pytest
import allure

@allure.title("Проверка функции LIST_CONTAINS")
def test_list_contains_function(login_leskov, run_function_test):
   login_leskov()
   run_function_test("list_contains([1, 3, 5, 6], 3)", 'true')