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


### Fetch historical cryptocurrency data

This function is a wrapper of https://developers.coinbase.com/api/v2#prices
* ***n***: integer, number of days we want since today
* **type**: str, ['buy', 'sell', 'spot']
* **currency_pair**: str, crypto & currency

```python
from autoforecast.datasets.import_bitcoin_price import get_price_for_last_n_days


crypto_df = get_price_for_last_n_days(
    n=1, type='spot', currency_pair='BTC-USD')
)
```