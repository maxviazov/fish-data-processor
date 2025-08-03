import pandas as pd


def preview_excel(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    print(df.columns)
    print(df.head())
    needs_columns = ['מספר עוסק מורשה', 'אסמכתת בסיס', "סה'כ אריזות", "סה'כ משקל"]
    # Check if all needed columns exist in the dataframe
    missing_columns = [col for col in needs_columns if col not in df.columns]
    if missing_columns:
        print(f"Warning: Missing columns: {missing_columns}")
        # Use only available columns
        available_columns = [col for col in needs_columns if col in df.columns]
        if available_columns:
            df_small = df[available_columns]
            print(df_small.head())
    else:
        df_small = df[needs_columns]
        print(df_small.head())
    return df
