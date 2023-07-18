import json
import sqlite3

import pandas as pd


def convertJson(jsonFile: str) -> pd.DataFrame:
    return pd.read_json(jsonFile)


def convertDf(databaseFile: str, tableName: str, df: pd.DataFrame) -> int:
    sqlite = sqlite3.connect(databaseFile)

    rows: int = df.to_sql(tableName, sqlite, if_exists="append")
    # sqlite.close()
    return rows


def main() -> None:
    df = convertJson(
        "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/metrics/example.json"
    )
    df.set_index("id", inplace=True)

    # print(df)
    print(convertDf("example.db", "scores", df))


main()
