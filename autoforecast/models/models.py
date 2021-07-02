from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor,
)
from sklearn.linear_model import LinearRegression, Ridge, SGDRegressor
from sklearn.svm import LinearSVR, SVR, NuSVR
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xgb

from autoforecast.models.neural_net import *
from autoforecast.models.naive import *
from autoforecast.models.time_series import *


def get_dict_models():
    dict_models = {
        "BaseKeras": BaseKeras(),
        "LSTMKeras": LSTMKeras(),
        "XGBRegressor": xgb.XGBRegressor(),
        "RandomForestRegressor": RandomForestRegressor(),
        "GradientBoostingRegressor": GradientBoostingRegressor(),
        "AdaBoostRegressor": AdaBoostRegressor(),
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(),
        "SGDRegressor": SGDRegressor(),
        "LinearSVR": LinearSVR(),
        "SVR": SVR(),
        "NuSVR": NuSVR(),
        "DecisionTreeRegressor": DecisionTreeRegressor(),
        "ExtraTreeRegressor": ExtraTreeRegressor(),
        "MLPRegressor": MLPRegressor(),
        "KNeighborsRegressor": KNeighborsRegressor(),
        "ARMA": ARMA(),
        #'BaselineLastYear': BaselineLastYear(),
        "BaselineLastValue": BaselineLastValue(),
        "BaselineMean": BaselineMean(),
        "BaselineMedian": BaselineMedian(),
        "Prophet": Prophet(),
    }
    return dict_models
