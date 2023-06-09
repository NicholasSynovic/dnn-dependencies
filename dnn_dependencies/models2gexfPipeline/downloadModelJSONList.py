from re import Match, search
from typing import List

import numpy
import pandas
from numpy import ndarray
from pandas import DataFrame, Series
from progress.spinner import Spinner
from requests import Response, get
from requests.structures import CaseInsensitiveDict


def searchForURL(query: str) -> str:
    pattern: str = r"<([^>]+)>"
    match: Match[str] = search(pattern=pattern, string=query)
    return match.group(1)


def main() -> None:
    url: str = "https://huggingface.co/api/models"

    dfList: List[DataFrame] = []
    with Spinner("Getting HuggingFace Hub JSON... ") as spinner:
        while True:
            resp: Response = get(url)
            df: DataFrame = DataFrame(data=resp.json())
            dfList.append(df)
            headers: CaseInsensitiveDict = resp.headers

            try:
                url = searchForURL(query=headers["link"])
            except KeyError:
                break

            spinner.next()

    df: DataFrame = pandas.concat(objs=dfList, ignore_index=True)

    mask: ndarray = df["id"].str.contains("/").to_numpy()

    ids: Series = df["id"]
    ids.mask(cond=mask, inplace=True)
    ids.dropna(inplace=True)

    with open("baseModels.txt", "w") as txt:
        txt.writelines(ids)
        txt.close()


if __name__ == "__main__":
    main()
