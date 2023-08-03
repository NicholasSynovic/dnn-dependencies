from typing import Type

from numpy import longdouble
from typedframe import TypedDataFrame


class ModelsDF(TypedDataFrame):
    schema: dict[str, Type[int] | Type[str]] = {
        "ID": int,
        "Model Name": str,
        "Model Filepath": str,
    }


class BaseModelsDF(TypedDataFrame):
    schema: dict[str, Type[int]] = {
        "ID": int,
        "Model_ID": int,
    }


class GraphPropertiesDF(TypedDataFrame):
    schema: dict[str, Type[int] | Type[longdouble]] = {
        "ID": int,
        "Model_ID": int,
        "Barycenter": longdouble,
        "Radius": longdouble,
        "DAG Longest Path Length": longdouble,
        "Average Shortest Path Length": longdouble,
        "Number of Isolates": longdouble,
        "Is Threshold Graph": longdouble,
        "Diameter": longdouble,
        "Attribute Assortativity Coefficient": longdouble,
        "Degree Pearson Correlation Coefficient": longdouble,
        "Number of Weakly Connected Components": longdouble,
        "Number of Strongly Connected Components": longdouble,
        "Number of Attracting Components": longdouble,
        "Is Semiconnected": longdouble,
        "Is Attracting Component": longdouble,
        "Is Strongly Connected": longdouble,
        "Is Weakly Connected": longdouble,
        "Is Triad": longdouble,
        "Is Regular": longdouble,
        "Is Planar": longdouble,
        "Is Distance Regular": longdouble,
        "Is Strongly Regular": longdouble,
        "Is Bipartite": longdouble,
        "Is Aperiodic": longdouble,
        "Is Directed Acyclic": longdouble,
        "Robins Alexander Clustering": longdouble,
        "Transitivity": longdouble,
        "Number of Nodes": longdouble,
        "Density": longdouble,
        "Number of Edges": longdouble,
        "Density": longdouble,
        "Number of Edges": longdouble,
        "Number of Communities": longdouble,
        "Degree Assortivity Coefficient": longdouble,
    }
