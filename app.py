import streamlit as st
import pandas as pd
import numpy as np
from data_processor import DataProcessor
from models import TimeSeriesForecaster
from visualizer import Visualizer
import io

def main():
    st.title("Financial Forecasting Application")
    
    # File upload
    uploaded_file = st.file_uploader("Upload financial data (CSV)", type="csv")
    
    if uploaded_file is not None:
        # Load and process data
        data_processor = DataProcessor()
        try:
            df = data_processor.load_data(uploaded_file)
            
            # Display raw data
            st.subheader("Raw Data Preview")
            st.dataframe(df.head())
            
            # Select target column
            target_column = st.selectbox(
                "Select the target column for forecasting",
                df.select_dtypes(include=[np.number]).columns
            )
            
            # Model parameters
            st.subheader("Forecast Parameters")
            forecast_period = st.slider("Forecast Period (days)", 7, 90, 30)
            model_type = st.selectbox(
                "Select Forecasting Model",
                ["Moving Average", "Simple Exponential Smoothing"]
            )
            
            if model_type == "Moving Average":
                window_size = st.slider("Window Size", 3, 30, 7)
                
            # Create forecaster instance
            forecaster = TimeSeriesForecaster()
            
            # Generate forecast
            if st.button("Generate Forecast"):
                with st.spinner("Generating forecast..."):
                    if model_type == "Moving Average":
                        forecast, metrics = forecaster.moving_average_forecast(
                            df[target_column],
                            window_size,
                            forecast_period
                        )
                    else:
                        forecast, metrics = forecaster.exponential_smoothing_forecast(
                            df[target_column],
                            forecast_period
                        )
                    
                    # Display metrics
                    st.subheader("Forecast Metrics")
                    for metric, value in metrics.items():
                        st.metric(metric, f"{value:.4f}")
                    
                    # Visualize results
                    visualizer = Visualizer()
                    fig = visualizer.plot_forecast(
                        df[target_column],
                        forecast,
                        model_type
                    )
                    st.plotly_chart(fig)
                    
                    # Export functionality
                    forecast_df = pd.DataFrame({
                        'Date': pd.date_range(
                            start=df.index[-1],
                            periods=forecast_period + 1,
                            closed='right'
                        ),
                        'Forecast': forecast
                    })
                    
                    csv = forecast_df.to_csv(index=False)
                    st.download_button(
                        label="Download Forecast CSV",
                        data=csv,
                        file_name="forecast.csv",
                        mime="text/csv"
                    )
                    
        except Exception as e:
            st.error(f"Error processing data: {str(e)}")
    
    else:
        st.info("Please upload a CSV file containing financial time series data")

if __name__ == "__main__":
    main()
