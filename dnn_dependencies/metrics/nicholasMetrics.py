import random

import numpy
from networkx import DiGraph, diameter, read_gexf
from networkx.algorithms.approximation import (average_clustering,
                                               metric_closure)
from networkx.algorithms.assortativity import (
    attribute_assortativity_coefficient, degree_assortativity_coefficient,
    degree_pearson_correlation_coefficient)
from networkx.algorithms.asteroidal import is_at_free
from networkx.algorithms.components import (
    is_attracting_component, is_semiconnected, is_strongly_connected,
    is_weakly_connected, number_attracting_components,
    number_strongly_connected_components, number_weakly_connected_components)
from progress.bar import Bar

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def _updateProgressBar(metric: str, bar: Bar) -> None:
    bar.message = bar.message.format(metric)
    bar.update()


def computeDiameter(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(metric="Graph Diameter", bar=bar)
    value: int = diameter(G=graph)
    bar.next()
    return value


def computeAverageClustering(graph: DiGraph, bar: Bar) -> float:
    _updateProgressBar(metric="Average Clustering", bar=bar)
    value: float = average_clustering(G=graph, trials=1000, seed=RANDOM_SEED)
    bar.next()
    return value


def computeMetricClosure(graph: DiGraph, bar: Bar) -> float:
    _updateProgressBar(metric="Metric Closure", bar=bar)
    value: float = metric_closure(G=graph)
    bar.next()
    return value


def computeDegreeAssortativityCoefficient(graph: DiGraph, bar: Bar) -> float:
    _updateProgressBar(metric="Degree Assortativity Coefficient", bar=bar)
    value: float = degree_assortativity_coefficient(G=graph, x="out", y="in")
    bar.next()
    return value


def computeAttributeAssortativityCoefficient(graph: DiGraph, bar: Bar) -> float:
    _updateProgressBar(
        metric="Attribute Assortativity Coefficient [Operation_Type]",
        bar=bar,
    )
    value: float = attribute_assortativity_coefficient(
        G=graph,
        attribute="Operation_Type",
    )
    bar.next()
    return value


def computeDegreePearsonCorrelationCoefficient(graph: DiGraph, bar: Bar) -> float:
    _updateProgressBar(
        metric="Degree Pearson Correlation Coefficient",
        bar=bar,
    )
    value: float = degree_pearson_correlation_coefficient(
        G=graph,
        x="out",
        y="in",
    )
    bar.next()
    return value


def computeIsAsteroidalTripleFree(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Is Asteroidal Triple Free",
        bar=bar,
    )
    value: int = int(is_at_free(G=graph))
    bar.next()
    return value


def computeIsSemiconnected(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Is Semiconnected",
        bar=bar,
    )
    value: int = int(is_semiconnected(G=graph))
    bar.next()
    return value


def computeIsAttractingComponent(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Is Attracting Component",
        bar=bar,
    )
    value: int = int(is_attracting_component(G=graph))
    bar.next()
    return value


def computeIsStronglyConnected(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Is Strongly Connected",
        bar=bar,
    )
    value: int = int(is_strongly_connected(G=graph))
    bar.next()
    return value


def computeIsWeaklyConnected(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Is Weakly Connected",
        bar=bar,
    )
    value: int = int(is_weakly_connected(G=graph))
    bar.next()
    return value


def computeNumberOfWeaklyConnectedComponents(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Number of Weakly Connected Components",
        bar=bar,
    )
    value: int = number_weakly_connected_components(G=graph)
    bar.next()
    return value


def computeNumberOfStronglyConnectedComponents(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Number of Strongly Connected Components",
        bar=bar,
    )
    value: int = number_strongly_connected_components(G=graph)
    bar.next()
    return value


def computeNumberOfAttracingComponents(graph: DiGraph, bar: Bar) -> int:
    _updateProgressBar(
        metric="Number of Attracting Components",
        bar=bar,
    )
    value: int = number_attracting_components(G=graph)
    bar.next()
    return value


def main() -> None:
    graph: DiGraph = read_gexf("file")


if __name__ == "__main__":
    main()
