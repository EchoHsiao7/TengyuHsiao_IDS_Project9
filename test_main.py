from main import hello


def test_hello():
    assert hello() == "Hello"


def test_hi():
    assert hello() != "hi"


if __name__ == "__main__":
    test_hello()
    test_hi()
    print("All tests passed.")
