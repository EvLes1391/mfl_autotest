import pytest

def test_if_function(login_leskov, run_function_test):
   login_leskov()
   run_function_test("list_contains([1, 3, 5, 6], 3)", 'true')