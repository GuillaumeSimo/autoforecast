
import os
print(os.getcwd())
from autoforecast import models


def test_model_naive():
    model = models.naive.BaselineMean()
    y_train = list(range(10))
    model.fit(X_train=None, y_train=y_train)
    X_test = [0] * 3
    y_pred = model.predict(X_test)
    assert y_pred == [4.5, 4.5, 4.5]


def test_base():
    assert True
