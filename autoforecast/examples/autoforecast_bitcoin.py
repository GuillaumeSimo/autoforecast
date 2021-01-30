# Forecasting/autoforecast/main.py
from autoforecast.automl import AutoForecast
from autoforecast.datasets.import_bitcoin_price import get_price_for_last_n_days


def run(verbose: bool):
    # settings
    # lists of features name
    list_cat_feat = ['timestamp']
    # lists of features name tokenized
    list_num_feat = []

    df_price = get_price_for_last_n_days(n=120, type='spot', currency_pair='BTC-USD')
    df_price = df_price.rename(columns={'price': 'target'})
    print(df_price)

    ind_cutoff = int(df_price.shape[0]* 0.8)
    train = df_price.iloc[:ind_cutoff]
    test = df_price.iloc[ind_cutoff:]
    print(train.shape, test.shape)

    cols = list_cat_feat + list_num_feat
    X_train = train[cols].values
    y_train = train['target'].values
    X_test = test[cols].values
    y_test = test['target'].values

    # main.py
    res_auto_forecast = AutoForecast(train).run_auto_forecast(
        X_train, y_train, X_test, y_test,
        verbose=verbose, max_time_in_sec=600
    )

    return res_auto_forecast
