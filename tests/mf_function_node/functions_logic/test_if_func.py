import pytest

def test_if_function(login_leskov, run_function_test):
    login_leskov()
    run_function_test('if(1 < 2, TRUE, false)', 'true')