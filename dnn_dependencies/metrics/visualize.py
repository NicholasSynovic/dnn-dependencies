from json import load

import pandas
from matplotlib import pyplot as plt
from pandas import DataFrame


def addlabels(x, y):
    # https://www.geeksforgeeks.org/adding-value-labels-on-a-matplotlib-bar-chart#tablist3-tab1
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha="center", bbox=dict(facecolor="red", alpha=0.8))


def main() -> None:
    with open("bert.json", "r") as jsonFile:
        json: dict = load(fp=jsonFile)
        jsonFile.close()

    npt: dict[str, int] = json["Node Pairing Distribution"]

    df: DataFrame = DataFrame().from_dict(data=npt, orient="index")
    df.reset_index(inplace=True)
    df.columns = ["Key", "Count"]
    df.dropna(inplace=True, ignore_index=True)

    df.plot.bar(x="Key", y="Count", figsize=(30, 10))

    addlabels(x=df["Key"], y=df["Count"])

    plt.title("Node Type Pairing Distribution (Bert Base Cased)")
    plt.xlabel(xlabel="Node Type Pairs")
    plt.ylabel(ylabel="Number of Pairs")
    plt.xticks(rotation=90)
    plt.tick_params(axis="x", which="major", labelsize=12)
    plt.tight_layout()

    plt.savefig("test.png")


if __name__ == "__main__":
    main()
