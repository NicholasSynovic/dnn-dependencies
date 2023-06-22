import json
import re

import matplotlib.pyplot as plt

with open("gpt2.json") as file:
    model1 = json.load(file)

with open("bert-base-cased.json") as file:
    model2 = json.load(file)


def count(model1: json, model2: json, metricLabel: str) -> plt:
    metric1 = model1[metricLabel]
    metric2 = model2[metricLabel]
    labels = ["Model1", "Model2"]
    counts = [metric1, metric2]
    colors = ["blue", "green"]
    plt.bar(labels, counts, color=colors)
    plt.title(metricLabel)
    plt.ylabel("Count")
    plt.xlabel("DL Model")
    plt.show()


def distribution(model1: json, model2: json, metricLabel: str, scale: str) -> plt:
    metric1 = model1[metricLabel]
    values1 = [float(key) for key in metric1.keys()]
    frequencies1 = [int(value) for value in metric1.values()]

    metric2 = model2[metricLabel]
    values2 = [float(key) for key in metric2.keys()]
    frequencies2 = [int(value) for value in metric2.values()]

    plt.bar(values1, frequencies1, alpha=0.5, label="Model 1", color="blue")
    plt.bar(values2, frequencies2, alpha=0.5, label="Model 2", color="green")
    input_string = metricLabel
    words = input_string.split()
    metric = " ".join(words[:2])
    plt.title(metricLabel)
    plt.ylabel("Node Count")
    plt.xlabel(metric)
    plt.yscale(scale)
    plt.legend()
    plt.show()


count(model1, model2, "Edge Count")

distribution(model1, model2, "Out Degree Distribution", "log")
