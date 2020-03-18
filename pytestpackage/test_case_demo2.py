import pytest

@pytest.fixture()
def setUp():
    print("once before every method")
    yield
    print("Once after every method")

def test_methodA(setUp):
    print("Running demo2 Method A")

def test_methodB(setUp):
    print("Running demo2 Method B")
