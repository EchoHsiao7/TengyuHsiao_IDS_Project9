import polars as pl
from main import read_data, generate_summary_statistics


def create_test_data():
    data = {"price": [2, 4, 6, 8, 10]}
    df = pl.DataFrame(data)
    return df


def test_read_data():
    df = create_test_data()
    assert isinstance(df, pl.DataFrame), "read_data should return a Polars DataFrame"


def test_generate_summary_statistics():
    df = create_test_data()
    mean, median, std = generate_summary_statistics(df, "price")

    expected_mean = 6
    expected_median = 6
    expected_std = 3.162

    assert (
        round(mean, 3) == expected_mean
    ), f"Expected mean: {expected_mean}, but got {mean}"
    assert (
        round(median, 2) == expected_median
    ), f"Expected median: {expected_median}, but got {median}"
    assert (
        round(std, 3) == expected_std
    ), f"Expected standard deviation: {expected_std}, but got {std}"


if __name__ == "__main__":
    test_read_data()
    test_generate_summary_statistics()
