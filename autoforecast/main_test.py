from autoforecast.datasets.import_bitcoin_price import get_price_for_last_n_days
from autoforecast.models.naive import BaselineMean
from autoforecast.src.utils.metrics import get_metrics
from autoforecast.automl import AutoForecast


df_price = get_price_for_last_n_days(n=30, type='spot', currency_pair='BTC-USD')
df_price = df_price.rename(columns={'price': 'target'})
print(df_price)

ind_cutoff = int(df_price.shape[0]* 0.8)
train = df_price[:ind_cutoff]
test = df_price[ind_cutoff:]

X_train = train['timestamp']
y_train = train.target
X_test = test['timestamp']
y_test = test.target


res_auto_forecast = AutoForecast(train).run_auto_forecast(
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test
)

print(res_auto_forecast)


#model = BaselineMean()
model.fit(X_train=X_train, y_train=y_train)

y_pred = model.predict(X_test=X_test)

metrics = get_metrics(y_test=y_test, y_pred=y_pred)
print(metrics)
