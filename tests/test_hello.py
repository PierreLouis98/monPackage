# tests/test_hello.py
from monPackage.lib import hello

def test_hello_length():
    assert hello("Thibault") == "Hello Thibault !"
