#%%
from src import pair_soporte as pair

import pandas as pd
# %%

df_ventas = pair.exploracion_csv('ventas.csv')
df_productos = pair.exploracion_csv('productos.csv')
df_clientes = pair.exploracion_csv('clientes.csv')

# %%
# A PARTIR DE AQUI SON FUNCIONES PARA LIMPIAR 

#pasamos los nombres de las oclumnas a minusucla 
df_clientes = pair.convert_minuscula(df_clientes)
df_productos = pair.convert_minuscula(df_productos)
df_ventas = pair.convert_minuscula(df_ventas)

# %%
#RENOMBRAR COLUMNAS 
df_productos = df_productos.reset_index()
nuevos_nombres = ['id', 'nombre_producto', 'categoría', 'precio', 'origen', 'descripción', 'descripción_2']

df_productos = pair.renombrar_columnas(df_productos, nuevos_nombres)

#%% 
# MODIFICAR COLUMNAS 

modif_col = pair.modificar_col_products(df_productos, "descripción_2")

#cambiamos los nombres de las columnas de productos porque están giradas. 
#%%

comb_cols = pair.combinar_columnas(df_productos, "descripción", "descripción_2", "all")
#%%
#eliminar columnas descripción y escripc 2
elim_col_prod = pair.eliminar_columns_prod(df_productos, "descripción", "descripción_2", "all")
#%%

nulls_country = pair.eliminar_nulls(df_clientes, "country")
#%%
columnas_nulls = ["gender", "email", "city", "address"]
nulls_unknown = pair.nulls_unknown(df_clientes, columnas_nulls)
#%%

unir_df = pair.mergear(df_clientes, df_ventas, df_productos)
# %%
