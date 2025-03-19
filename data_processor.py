import pandas as pd

class DataProcessor:
    def load_data(self, file):
        """
        Load and preprocess time series data
        """
        # Read CSV file
        df = pd.read_csv(file)
        
        # Check for date column
        date_columns = df.select_dtypes(include=['datetime64']).columns
        if len(date_columns) == 0:
            # Try to identify date column
            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col])
                    df.set_index(col, inplace=True)
                    break
                except:
                    continue
            if df.index.dtype != 'datetime64[ns]':
                raise ValueError("No valid date column found in the dataset")
        else:
            df.set_index(date_columns[0], inplace=True)
            
        # Sort by date
        df.sort_index(inplace=True)
        
        # Handle missing values
        df.interpolate(method='linear', inplace=True)
        
        return df
