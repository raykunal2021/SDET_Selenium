import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram(setup):
    msg = "Hello" #operations
    assert msg == "Hello", "Test failed because strings do not match"



def test_SecondCreditCard(setup):
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"




@pytest.mark.xfail
def test_SecondGreetCreditCard1(setup):
    print("Good Morning")




def test_fixtureDemo(setup):
    print(" i will execute steps of fixturedemo method")