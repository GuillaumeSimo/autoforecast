# Auto Forecast
AutoML library for time series forecasting

## Quick start

Upgrade pip
```bash
$ pip install pip --upgrade
```

Install autoforecast
```bash
$ pip install autoforecast
```


### Try it out with your own dataset
```python
from autoforecast.automl import AutoForecast


model = AutoForecast()

print('Autoforecast() model fitting...')
model.fit(X_train=X_train, y_train=y_train)

print('Autoforecast() model predicting...')

y_pred = model.predict(X_test=X_test)
print(f'y_pred={y_pred})
```


### Run the example function
```python
from autoforecast.examples import autoforecast_bitcoin


autoforecast_bitcoin.run()
```