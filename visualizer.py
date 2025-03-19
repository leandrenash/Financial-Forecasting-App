import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Visualizer:
    def plot_forecast(self, historical, forecast, model_type):
        """
        Create interactive visualization of historical data and forecast
        """
        fig = make_subplots(rows=1, cols=1)
        
        # Plot historical data
        fig.add_trace(
            go.Scatter(
                y=historical,
                name="Historical Data",
                line=dict(color="blue")
            )
        )
        
        # Plot forecast
        forecast_dates = pd.date_range(
            start=historical.index[-1],
            periods=len(forecast) + 1,
            closed='right'
        )
        
        fig.add_trace(
            go.Scatter(
                x=forecast_dates,
                y=forecast,
                name=f"{model_type} Forecast",
                line=dict(color="red", dash="dash")
            )
        )
        
        # Update layout
        fig.update_layout(
            title=f"Financial Forecast using {model_type}",
            xaxis_title="Date",
            yaxis_title="Value",
            showlegend=True,
            hovermode="x"
        )
        
        return fig
