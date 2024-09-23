"""
This module reads a csv file and produce some useful statistics from it.
"""


import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv("Steam_2024_bestRevenue_1500.csv")
    mean_values = df["price"].mean(numeric_only=True)
    median_values = df["price"].median(numeric_only=True)
    std_values = df["price"].std(numeric_only=True)
    print("Price:\n")
    print("Mean:\n", mean_values)
    print("\nMedian:\n", median_values)
    print("\nStandard Deviation:\n", std_values)

    plt.hist(df["price"].dropna(), bins=20, edgecolor="k")
    plt.title("Histogram of price")
    plt.xlabel("price")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")
    plt.show()

    mean_values = df["revenue"].mean(numeric_only=True)
    median_values = df["revenue"].median(numeric_only=True)
    std_values = df["revenue"].std(numeric_only=True)

    print("revenue:\n")
    print("Mean:\n", mean_values)
    print("\nMedian:\n", median_values)
    print("\nStandard Deviation:\n", std_values)

    plt.scatter(
        df["price"], df["revenue"], alpha=0.5, edgecolors="w", label="Price vs Revenue"
    )
    plt.title("Scatter Plot of Price vs Revenue")
    plt.xlabel("Price")
    plt.ylabel("Revenue")
    plt.legend()
    plt.grid(True)
    plt.show()
