from skopt.space import Categorical, Integer, Real


prophet_x0 = [0.05, 10, 'additive']
prophet_space = [
    Real(low=0.001, high=0.5, name='changepoint_prior_scale'),
    Real(low=0.01, high=10.0, name='seasonality_prior_scale'),
    Categorical(['additive', 'multiplicative'], name='seasonality_mode')
]


sarimax_x0 = [0.05, 10]
sarimax_space = [
    Real(low=0.001, high=0.5, name='changepoint_prior_scale'),
    Real(low=0.01, high=10.0, name='seasonality_prior_scale')
]
