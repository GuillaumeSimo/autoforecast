from typing import List, Optional

import pandas as pd

from autoforecast.preprocessing import (
    categorical, engineering, features_selection, numerical
)


def preprocessing(
    df,
    target_name: List[str],
    categoricals: List[str],
    numericals: List[str],
    date_col: Optional[str] = None,
    train_size: float = 0.7,
    engineering: bool = True,
    selection: bool = True
):
    cutoff = int(len(df) * train_size)
    train, test = df[:cutoff], df[cutoff:]

    train_cat, test_cat = categorical.run(
        df=df, list_cat_feat=categoricals, date_col=date_col
    )
    train_num, test_num = numerical.run(df=df, list_num_feat=numericals)
    #TBD engineering.run()
    train_concat = pd.concat([train_cat, train_num], axis=1)
    test_concat = pd.concat([test_cat, test_num], axis=1)
    train_selected, test_selected = features_selection.run(
        train_concat, test_concat
    )
    X_train = train_selected.drop('target', axis=1).values
    y_train = train_selected['target'].values
    X_test = test_selected.drop('target', axis=1).values
    y_test = test['target'].values
    return X_train, y_train, X_test, y_test