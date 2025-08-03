from typing import List

import pandas as pd


def preview_excel(file_path: str, needs_columns: List[str] = None, n: int = 5) -> pd.DataFrame:
    """
    Reads Excel, prints columns and head, returns DataFrame with only needed columns if available.
    """
    df = pd.read_excel(file_path)
    print("Все столбцы файла:")
    print(list(df.columns))
    print(f"\nПервые {n} строк файла:")
    print(df.head(n))

    if needs_columns:
        missing_columns = [col for col in needs_columns if col not in df.columns]
        if missing_columns:
            print(f"\n⚠️ Warning: Missing columns: {missing_columns}")
        available_columns = [col for col in needs_columns if col in df.columns]
        if available_columns:
            df_small = df[available_columns]
            print(f"\nТолько выбранные столбцы ({available_columns}):")
            print(df_small.head(n))
            return df_small
        else:
            print("❌ Нет ни одного нужного столбца!")
            return pd.DataFrame()  # пустой DataFrame
    return df