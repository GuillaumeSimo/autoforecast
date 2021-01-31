from typing import Callable

from skopt import gp_minimize
from skopt.utils import use_named_args


class HyperparametersTuner():
    def __init__(
        self,
        model: Callable,
        search_space: list,
        x0: list,
        metric: Callable
    ):
        self.model = model
        self.search_space = search_space
        self.x0 = x0
        self.metric = metric

    def __call__(self):
        return self.optimize()

    def optimize(
        self,
        X_train,
        X_test,
        y_train,
        y_test,
        n_calls: int = 10,
        n_random_starts: int = 3,
        random_state: int = 666
    ):
        dimensions = self.search_space
        print(dimensions)

        @use_named_args(dimensions=dimensions)
        def fitness(**params):
            print(f'params={params}')
            model = self.model(**params)
            model.fit(X_train, y_train, params)

            y_pred = model.predict(X_test)
            metric_value = self.metric(y_test, y_pred)
            return -1.0 * metric_value

        res = gp_minimize(func=fitness,
                          dimensions=dimensions,
                          acq_func='EI',  # Expected Improvement.
                          x0=self.x0,
                          n_calls=n_calls,
                          n_random_starts=n_random_starts,
                          random_state=random_state)
        print(f'best accuracy={-1.0 * res.fun} with {res.x}')
        return res
