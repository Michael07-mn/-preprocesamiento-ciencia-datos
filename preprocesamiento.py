import pandas as pd

def cargar_dataset(ruta):
    """Carga un dataset desde un archivo .CSV"""
    return pd.read_csv(ruta)

def limpiar_nulos(df):
    """Elimina filas con valores nulos"""
    return df.dropna()

def normalizar_columnas(df, columnas):
    """Normaliza columnas numéricas"""
    for col in columnas:
        df[col] = (df[col] - df[col].mean()) / df[col].std()
    return df
