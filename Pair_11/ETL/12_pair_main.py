#%%
from src import pair_bbdd_soporte as bbdd
from src import queries_bbdd as queries
import pandas as pd 
#%%
df=pd.read_csv('ventas.csv')

#%%
lista_tuplas_ventas = []
for x in df.values:

    lista_tuplas_ventas.append(tuple(x))
    lista_tuplas_ventas
# %%
## Hemos creado la base de datos en sql y también la tabla ventas. 

bbdd.insertar_datos(queries.query_insertar_ventas, 'AlumnaAdalab', 'pair_12', lista_tuplas_ventas)
# %%
