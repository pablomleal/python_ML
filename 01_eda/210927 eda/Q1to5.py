import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

filepath = 'ml/210927 eda/iris_data.csv'

datos = pd.read_csv(filepath)


#QUESTION 1
#print ("SHAPE:", datos.shape, "\n", sep='\n')
print ("COLUMNS: ", datos.columns,"\n",  sep='\n')
#print ("DTYPES: ", datos.dtypes, "\n", sep='\n')
#print ("Data Head: ", datos.head, "\n", sep='\n') 

##QUESTION 2 (NOT APPLICABLE)

##QUESTION 3
#print("Número de mediciones por especie: \n", datos.iloc[:,4].value_counts(), '\n')

metrics = datos.describe()
metrics.loc['range'] = metrics.apply(lambda x: x['max'] - x['min'])
#print("Resultados globales: \n", metrics)



##QUESTION 4
#print(datos.iloc[:,1])
groupBySpecies = datos.groupby(['species'])

media = groupBySpecies.mean()
#print ("Media: \n", media, "\n")

mediana = groupBySpecies.median()
#print ("Mediana: \n", mediana, "\n")

combined = groupBySpecies.agg([np.mean, np.median])
#print("Combinados: \n", combined)


