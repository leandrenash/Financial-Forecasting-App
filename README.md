# Financial Forecasting App

![forecast-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/819995eb-ed44-42ca-be85-c65fed1f63e3)


## Overview
This Streamlit-based application provides interactive financial time series forecasting capabilities. It allows users to upload financial data, visualize trends, and generate forecasts using various statistical models.

## Features
- **Data Upload**: Support for CSV files containing time series financial data
- **Interactive Visualization**: Dynamic plots showing historical data and forecasts
- **Multiple Forecasting Models**:
  - Moving Average
  - Simple Exponential Smoothing
- **Performance Metrics**:
  - Mean Absolute Error (MAE)
  - Root Mean Square Error (RMSE)
  - Mean Absolute Percentage Error (MAPE)
- **Export Functionality**: Download forecasts as CSV files

## Installation
The application requires Python 3.11+ and the following dependencies:
- streamlit
- pandas
- numpy
- plotly
- scikit-learn

To install dependencies:
```bash
pip install streamlit pandas numpy plotly scikit-learn
```

## Usage Guide

### 1. Data Preparation
Prepare your financial data in CSV format with:
- A date/timestamp column
- Numerical columns for forecasting

Example CSV format:
```csv
Date,Value
2024-01-01,100.5
2024-01-02,101.2
...
```

### 2. Running the Application
```bash
streamlit run app.py
```

### 3. Using the Interface
1. **Upload Data**:
   - Click "Upload financial data (CSV)"
   - Select your prepared CSV file

2. **Configure Forecast**:
   - Select target column for forecasting
   - Choose forecast period (7-90 days)
   - Select forecasting model:
     - Moving Average: Set window size (3-30 days)
     - Simple Exponential Smoothing

3. **Generate Forecast**:
   - Click "Generate Forecast" button
   - View performance metrics
   - Examine interactive visualization
   - Download forecast results

## Technical Details

### Components
- `app.py`: Main application interface
- `data_processor.py`: Data loading and preprocessing
- `models.py`: Forecasting models implementation
- `visualizer.py`: Interactive plotting functions

### Data Processing
- Automatic date column detection
- Missing value interpolation
- Time series sorting and validation

### Visualization
- Interactive Plotly charts
- Historical data and forecast overlay
- Customizable plot styling

## Future Enhancements
- Advanced forecasting models (ARIMA, Prophet)
- External economic indicators integration
- Enhanced visualization options
- Model parameter optimization

## Limitations
- Currently supports basic forecasting models
- Requires well-formatted CSV input
- Limited to single variable forecasting

## Contributing
Feel free to submit issues and enhancement requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
