import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

class TimeSeriesForecaster:
    def moving_average_forecast(self, series, window_size, forecast_period):
        """
        Generate forecast using Moving Average method
        """
        # Calculate moving average
        ma = series.rolling(window=window_size).mean()
        
        # Generate forecast
        last_ma = ma.iloc[-1]
        forecast = np.repeat(last_ma, forecast_period)
        
        # Calculate metrics
        valid_ma = ma[window_size:]
        metrics = self._calculate_metrics(series[window_size:], valid_ma)
        
        return forecast, metrics
    
    def exponential_smoothing_forecast(self, series, forecast_period, alpha=0.3):
        """
        Generate forecast using Simple Exponential Smoothing
        """
        # Initialize variables
        result = [series.iloc[0]]
        
        # Calculate exponential smoothing
        for n in range(1, len(series)):
            result.append(alpha * series.iloc[n] + (1 - alpha) * result[n-1])
        
        # Generate forecast
        last_value = result[-1]
        forecast = np.repeat(last_value, forecast_period)
        
        # Calculate metrics
        metrics = self._calculate_metrics(series[1:], pd.Series(result[1:]))
        
        return forecast, metrics
    
    def _calculate_metrics(self, actual, predicted):
        """
        Calculate forecast accuracy metrics
        """
        mae = mean_absolute_error(actual, predicted)
        mse = mean_squared_error(actual, predicted)
        rmse = np.sqrt(mse)
        mape = np.mean(np.abs((actual - predicted) / actual)) * 100
        
        return {
            "Mean Absolute Error": mae,
            "Root Mean Square Error": rmse,
            "Mean Absolute Percentage Error": mape
        }
