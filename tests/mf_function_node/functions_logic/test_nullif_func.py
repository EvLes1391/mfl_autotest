import pytest

def test_nullif_function(login_leskov, run_function_test):
   login_leskov()
   run_function_test("nullif(5, 5)", 'NULL')