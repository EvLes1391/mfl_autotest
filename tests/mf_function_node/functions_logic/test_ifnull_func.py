import pytest

def test_if_function(login_leskov, run_function_test):
   login_leskov()
   run_function_test("ifnull(null, 'это нулл')", 'это нулл')