# Forecasting/autoforecast/src/models/time_series_models.py
import datetime

import fbprophet
import numpy as np
import pandas as pd
import statsmodels.api as sm
from autoforecast import metrics
from autoforecast.configs.configspace.time_series_space import prophet_space, prophet_x0
from autoforecast.models.hyperparameters import HyperparametersTuner


class ARMA:
    def __init__(self, order=None, period=None):
        self.order = order

    def fit(self, X_train, y_train):
        self.y_train = y_train
        aic_matrix = self.build_aic(
            y_train=self.y_train, X_train=X_train, p_max=6, q_max=6, p_min=0, q_min=0
        )
        self.order = self.best_order(aic_matrix)

    def predict(self, X_test, *arg):
        y_pred = self.predict_arma(y_train=self.y_train, nforecast=len(X_test), order=self.order)
        return y_pred

    @staticmethod
    def build_aic(y_train: np.ndarray, X_train: np.ndarray, p_max=6, q_max=6, p_min=0, q_min=0):
        aic_full = pd.DataFrame(np.zeros((6, 6), dtype=float))
        # Iterate over all ARMA(p,q) models with p,q in [0,6]
        for p in range(6):
            for q in range(6):
                if p == 0 and q == 0:
                    continue
                # Estimate the model with no missing datapoints
                mod = sm.tsa.statespace.SARIMAX(
                    y_train, exog=X_train, order=(p, 0, q), enforce_invertibility=False
                )
                try:
                    res = mod.fit(disp=False, maxiter=200)
                    aic_full.iloc[p, q] = res.aic
                except Exception as e:
                    print(e)
                    aic_full.iloc[p, q] = np.nan
        return aic_full

    @staticmethod
    def best_order(aic_full: pd.DataFrame):
        aic_full.iloc[0, 0] = 10.0 ** 99
        # min column
        min_col_name = aic_full.min().idxmin()
        # min column index if needed
        min_col_idx = aic_full.columns.get_loc(min_col_name)
        # min row index
        min_row_idx = aic_full[min_col_name].idxmin()
        return (min_row_idx, 0, min_col_idx)

    @staticmethod
    def predict_arma(y_train: np.ndarray, nforecast: int, order=(1, 0, 1)):
        mod = sm.tsa.statespace.SARIMAX(y_train, order=order)
        res = mod.fit(disp=False)
        # In-sample one-step-ahead predictions, and out-of-sample forecasts
        predict = res.get_prediction(end=mod.nobs + nforecast)
        y_pred = predict.predicted_mean[-nforecast:]
        return np.array(y_pred)


class Prophet:
    def __init__(self):
        self.model = None
        self.period = None

    def fit(self, X_train, y_train, **params):
        numdays = len(X_train)
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
        df = pd.DataFrame({"ds": date_list, "y": y_train})
        self.model = fbprophet.Prophet(**params)
        self.model.fit(df)

    def predict(self, X_test):
        self.period = len(X_test)
        future = self.model.make_future_dataframe(periods=self.period, freq="M")
        forecast = self.model.predict(future)
        y_pred = forecast.yhat[-self.period :]
        return y_pred.values

    def optimize(self, X_train, X_test, y_train, y_test):
        return HyperparametersTuner(
            model=Prophet,
            search_space=prophet_space,
            x0=prophet_x0,
            metric=metrics.smape_score,
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test,
        )()
