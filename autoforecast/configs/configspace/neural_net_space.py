from skopt.space import Real, Integer


base_keras_x0 = [3]
base_keras_space = [
    Integer(low=3, high=100, name='hidden_size_dense')
]

lstm_keras_x0 = [3]
lstm_keras_space = [
    Integer(low=3, high=100, name='hidden_size_lstm')
]
