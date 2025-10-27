from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from sklearn.metrics import mean_squared_error
import math

"""
ARIMA = AutoRegressive Integrated Moving Average

un modèle combinant :

AR (Auto-Regressive) : dépendance linéaire entre la valeur actuelle et ses valeurs passées.

I (Integrated) :  différenciation de la série pour la rendre stationnaire.

MA (Moving Average) : dépendance linéaire entre la valeur actuelle et les erreurs passées.

"""
"""
Paramètres (p, d, q) :
Manuellement en observant :
les ACF (autocorrélation) et PACF (autocorrélation partielle) plots.
la stationnarité (test ADF).
"""

# print(model_auto.summary())
def fit_arima(train_series, order):
    model = ARIMA(train_series, order=order)
    model_fit = model.fit()
    return model_fit


def evaluate_forecast(y_true, y_pred):
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    return {'rmse': rmse}