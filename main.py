import matplotlib.pyplot as plt
import polars as pl


def read_data(file):
    df = pl.read_csv(file)
    return df


def generate_summary_statistics(dataframe, col_name):
    # Mean
    mean_value = dataframe[col_name].mean()
    # Median
    median_value = dataframe[col_name].median()
    # Standard deviation
    std_value = dataframe[col_name].std()

    print(f"Summary Statistics for {col_name}:")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_value}")

    return mean_value, median_value, std_value


def create_visualization(dataframe, col_name):
    data = dataframe[col_name].to_list()

    plt.hist(data, bins=20, alpha=0.7, color="blue")
    plt.title(f"Distribution of {col_name}")
    plt.xlabel(col_name)
    plt.ylabel("Frequency")
    plt.savefig("img/histogram.png")
    print("Histogram saved as 'histogram.png'")
    plt.show()


if __name__ == "__main__":
    input_file = "Steam_2024_bestRevenue_1500.csv"
    df_data = read_data(input_file)
    colname = "price"  # Replace with the actual column name
    mean, median, std = generate_summary_statistics(df_data, colname)
    create_visualization(df_data, colname)
