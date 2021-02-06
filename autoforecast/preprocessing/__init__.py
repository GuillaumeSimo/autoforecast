from typing import List

from Autoforecast.preprocessing import (
    categorical, engineering, features_selection, numerical
)


def preprocessing(
    df,
    target_name: List[str],
    categoricals: List[str],
    numericals: List[str],
    train_size: float,
    engineering: bool,
    selection: bool
):
    cutoff = int(len(df) * train_size)
    train, test = df[:cutoff], df[cutoff:]
