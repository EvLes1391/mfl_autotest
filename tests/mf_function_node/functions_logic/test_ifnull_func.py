import pytest
import allure

@allure.title("Проверка функции IFNULL")
def test_ifnull_function(login_leskov, run_function_test):
   login_leskov()
   run_function_test("ifnull(null, 'это нулл')", 'это нулл')