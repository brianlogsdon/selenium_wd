import pytest

@pytest.fixture()
def setUp():
    print("once before every method")

def test_methodA(setUp):
    print("Running demo1 Method A")

def test_methodB(setUp):
    print("Running demo1 Method B")

