import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print(" i will execute steps of fixturedemo method")

    def test_fixtureDemo1(self):
        print(" i will execute steps of fixturedemo method2")

    def test_fixtureDemo3(self):
        print(" i will execute steps of fixturedemo method3")


    def test_fixtureDemo4(self):
        print(" i will execute steps of fixturedemo method4")