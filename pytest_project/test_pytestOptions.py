import os

import pytest

@pytest.mark.login

def test_regression():
    print("lets test regression suite")
@pytest.mark.login
def test_sanity():
    print("lets test sanity suite")
@pytest.mark.login
@pytest.mark.func
def test_functional():
    print("lets test funtional suite")

def test_api():
    print("lets test api suite")
@pytest.mark.func
def test_functional1():
    print("lets test funtional suite")
@pytest.mark.skip(reason="taking ling time")
def test_functional2():
    print("lets test funtional suite")

@pytest.mark.skipif(os.name=='nt',reason='skip if the os is nt')
def test_functional3():
    print("lets test funtional suite!!:: "+os.name)