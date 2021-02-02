from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression, Ridge, SGDRegressor
from sklearn.svm import LinearSVR, SVR, NuSVR
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xgb


class BaseMLRegressor():
    def __init__(self):
        pass

    def fit(self):
        self.model.fit()

    def predic(self):
        self.model.predict()

    def optimize(
        self,
        X_train,
        X_test,
        y_train,
        y_test
    ):
        return HyperparametersTuner(
            model=LSTMKeras,
            search_space=lstm_keras_space,
            x0=lstm_keras_x0,
            metric=metrics.smape_score,
            X_train=X_train,
            X_test=X_test,
            y_train=y_train,
            y_test=y_test
        )()
