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
        Column(name="Model Name", type_=String),
        Column(name="Model Filepath", type_=String),
    )


def createSchema_BaseModels(
    metadata: MetaData, tableName: str = "Base Models", fkTableName: str = "Models"
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


def createSchema_ModelProperties(
    metadata: MetaData,
    tableName: str = "Model Properties",
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
