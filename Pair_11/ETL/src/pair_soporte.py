#%%
import pandas as pd   
import os 
import sys 
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames
# %%
def exploracion_csv(archivo):
    try: 
        dataframe=pd.read_csv(archivo, index_col=None, on_bad_lines='skip')
        #on bad lines skip para poder abrir fichero productos separado por columnas
    except: 
        df=pd.read_csv(archivo, sep=';', index_col=None, on_bad_lines='skip')
        dataframe=df.apply(pd.Series)
    
    display(dataframe.head())

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    
    
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
   

    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())    
    
    print("Los valores que tenemos para las columnas numéricas son: ")
    dataframe_numericas = dataframe.select_dtypes(exclude='O')
    
    try: 
        print("\n ..................... \n")
        print(f"Los principales estadísticos de las columnas categóricas son: ")
        display(dataframe_categoricas.describe(include = "O").T)
    except: 
        print('No hay columnas categóricas')
        
    try:
        print("\n ..................... \n")
        print(f"Los principales estadísticos de las columnas numéricas son: ")
        display(dataframe_numericas.describe().T)
    except: 
        print('No hay columnas numéricas')
        
    
        
    return dataframe
#%%
# A PARTIR DE AQUI SON FUNCIONES PARA LIMPIAR 
#columnas a minúsculas y quitar espacios
def convert_minuscula(dataframe):
    nuevas_columnas = {columna: columna.lower().strip() for columna in dataframe.columns}
    dataframe.rename(columns=nuevas_columnas, inplace=True)
    return dataframe
#%%


#CAMBIAR renombrar DE PRODUCTOS
def renombrar_columnas(dataframe, nuevos_nombres):
    nombres_actuales = dataframe.columns.tolist()
    mapeo_nombres = dict(zip(nombres_actuales, nuevos_nombres))
    dataframe.rename(columns=mapeo_nombres, inplace=True)
    return dataframe


# %%
# modificar columnas 
def modificar_col_products(dataframe, columna): 
    dataframe[columna].fillna('', inplace=True)
    return dataframe

# %%
def combinar_columnas(dataframe, columna1, columna2, nueva_columna):
    dataframe[nueva_columna] = dataframe[columna1] + ' - ' + dataframe[columna2]
    return dataframe

# %%
def eliminar_columns_prod(dataframe, columna1, columna2, columna3):
    dataframe.drop(columns=[columna1, columna2], axis=1, inplace=True)
    dataframe.rename(columns={columna3: columna1}, inplace=True)
    return dataframe 

#%%
def eliminar_nulls(dataframe, columna): 
    dataframe[columna] = dataframe[columna].fillna(dataframe[columna].mode()[0])
    return dataframe


def nulls_unknown(dataframe, lista_columnas):
    for columna in lista_columnas: 
        dataframe[columna]= dataframe[columna].fillna("unknown")
    return dataframe


def mergear (dataframe1, dataframe2, dataframe3):
    df_combinado = dataframe1.merge(dataframe2, left_on="id", right_on="id_cliente")
    df_combinado.drop(columns=["id_cliente"], inplace=True)
    df_combinado.set_index(["id_producto"], inplace=True)
    dataframe3.rename(columns={'id': 'id_producto'}, inplace=True)
    df_final = df_combinado.merge(dataframe3, on = "id_producto", how="left")
    df_final.to_csv("tabla_final_pair11.csv")

    return df_final