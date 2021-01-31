from skopt.space import Real, Integer

x0 = []

DIM_rf = [
    Integer(low=20, high=50, name='n_estimators'),
    Integer(low=10, high=50, name='max_depth'),
    Integer(low=1, high=4, name='min_samples_leaf'),
    Integer(low=2, high=10, name='min_samples_split')
]