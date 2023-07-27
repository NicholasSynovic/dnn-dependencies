from sqlalchemy import (Column, Engine, Float, ForeignKey, Integer, MetaData,
                        String, Table, create_engine)


def createEngine(path: str) -> Engine:
    """


    :param path: str:

    """
    return create_engine(url=path)


def schema_ModelStats(metadata: MetaData) -> Table:
    """


    :param metadata: MetaData:

    """
    table: Table = Table(
        "ModelStats",
        metadata,
        Column("ID", Integer, primary_key=True),
        Column("Model Name", String),
        Column("Model Filepath", String),
        Column("Is Semiconnected", String),
        Column("Is Attracting Component", String),
        Column("Is Strongly Connected", Integer),
        Column("Is Weakly Connected", Integer),
        Column("Is Triad", Integer),
        Column("Is Regular", Integer),
        Column("Is Planar", Integer),
        Column("Is Distance Regular", Integer),
        Column("Is Strongly Regular", Integer),
        Column("Is Bipartite", Integer),
        Column("Is Aperiodic", Integer),
        Column("Is Directed Acyclic", Integer),
        Column("Radius", Integer),
        Column("DAG Longest Path Length", Integer),
        Column("Number of Isolates", Integer),
        Column("Robins Alexander Clustering", Float),
        Column("Transitivity", Float),
        Column("Number of Nodes", Integer),
        Column("Density", Float),
        Column("Number of Edges", Integer),
        Column("Number of Communities", Integer),
        Column("Degree Assortivity Coefficient", Float),
        Column("Attribute Assortivity Coefficient", Float),
        Column("Number of Weakly Connected Components", Integer),
        Column("Number of Strongly Connected Components", Integer),
        Column("Number of Attracting Components", Integer),
        Column("Barycenter", Integer),
        Column("Degree Pearson Correlation Coefficient", Float),
    )
    return table


def schema_BaseModels(metadata: MetaData) -> Table:
    """


    :param metadata: MetaData:

    """
    table: Table = Table(
        "baseModels",
        metadata,
        Column("ID", Integer, primary_key=True),
        Column("Model ID", Integer, ForeignKey("ModelStats.ID")),
    )
    return table


def createTables(metadata: MetaData, engine: Engine) -> None:
    """


    :param metadata: MetaData:
    :param engine: Engine:

    """
    metadata.create_all(bind=engine)
