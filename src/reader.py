import pandas as pd


def preview_excel(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    print(df.columns)
    print(df.head())
    return df
