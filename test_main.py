def test_hello():
    assert "Hello" == "Hello"


def test_hi():
    assert "hello" != "hi"


if __name__ == "__main__":
    test_hello()
    test_hi()
    print("All tests passed.")
