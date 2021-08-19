import pandas as pd

#DATA TRANSFORMATION/VALIDATION
def data_validation(df: pd.DataFrame) -> bool: 
    if df.empty:
        print('\n* No songs were downloaded *\n ')
        return False

    if not pd.Series(df["played_at"]).is_unique:
        print('\n* Primary key check violated. Terminating extraction *\n ')

    #Check for null values
    if df.isnull().values.any():
        raise Exception('\n* Null values found. Terminating extraction *\n ')

    return True
