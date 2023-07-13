import json
import sqlite3

import pandas as pd


def convertJson(jsonFile: str) -> pd.DataFrame:
    return pd.read_json(jsonFile)


def convertDf(databaseFile: str, tableName: str, df: pd.DataFrame) -> None:
    sqlite = sqlite3.connect(databaseFile)
    return df.to_sql(tableName, sqlite, if_exists="replace")


def main() -> None:
    df = convertJson(
        "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/metrics/example.json"
    )
    print(convertDf("example.db", "example", df))


main()
