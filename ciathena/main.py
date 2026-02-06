import pytest
import os
import sys
#from ciathena.tests.test_Login import test_login_functionality

def test_run_all_tests():
    pytest.main([
         # "tests/test_Login.py",
         "tests/test_OngoingThreads.py",
         "tests/test_Insights.py",
         "tests/test_CollabSpace.py",
         "tests/test_Configurations.py",
         # "tests/test_Branding.py",
         # "tests/test_Athentication.py",
         # "tests/test_Users.py"
        # run entire test folder
        "-sv",
        "--alluredir=allure-results", # generate allure raw results
        "--clean-alluredir",         # clean old results
        "--headed",
    ])

if __name__ == "__main__":
    test_run_all_tests()


