from sqlalchemy import (Column, Connection, Float, ForeignKey, Integer,
                        MetaData, String, Table)


def closeConnection(conn: Connection) -> bool:
    conn.close()
    return conn.closed


def createSchema_Models(metadata: MetaData, tableName: str = "Models") -> None:
    Table(
        tableName,
        metadata,
        Column(
            "ID",
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
        ),
        Column("Model Name", String),
        Column("Model Filepath", String),
    )


def createSchema_BaseModels(
    metadata: MetaData,
    tableName: str = "Base Models",
    fkTableName: str = "Models",
) -> None:
    Table(
        tableName,
        metadata,
        Column(
            "ID",
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
        ),
        Column(
            "Model_ID",
            Integer,
            ForeignKey(f"{fkTableName}.ID"),
            unique=True,
        ),
    )


def createSchema_GraphProperties(
    metadata: MetaData,
    tableName: str = "Graph Properties",
    fkTableName: str = "Models",
) -> None:
    Table(
        tableName,
        metadata,
        Column(
            "ID",
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
        ),
        Column(
            "Model_ID",
            Integer,
            ForeignKey(f"{fkTableName}.ID"),
            unique=True,
        ),
        Column("Barycenter", Float),
        Column("Radius", Float),
        Column("DAG Longest Path Length", Float),
        Column("Average Shortest Path Length", Float),
        Column("Number of Isolates", Float),
        Column("Is Threshold Graph", Float),
        Column("Diameter", Float),
        Column("Attribute Assortativity Coefficient", Float),
        Column("Degree Pearson Correlation Coefficient", Float),
        Column("Number of Weakly Connected Components", Float),
        Column("Number of Strongly Connected Components", Float),
        Column("Number of Attracting Components", Float),
        Column("Is Semiconnected", Float),
        Column("Is Attracting Component", Float),
        Column("Is Strongly Connected", Float),
        Column("Is Weakly Connected", Float),
        Column("Is Triad", Float),
        Column("Is Regular", Float),
        Column("Is Planar", Float),
        Column("Is Distance Regular", Float),
        Column("Is Strongly Regular", Float),
        Column("Is Bipartite", Float),
        Column("Is Aperiodic", Float),
        Column("Is Directed Acyclic", Float),
        Column("Robins Alexander Clustering", Float),
        Column("Transitivity", Float),
        Column("Number of Nodes", Float),
        Column("Density", Float),
        Column("Number of Edges", Float),
        Column("Number of Communities", Float),
        Column("Degree Assortivity Coefficient", Float),
    )
