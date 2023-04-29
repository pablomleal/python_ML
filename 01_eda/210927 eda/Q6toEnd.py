import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

filepath = 'ml/210927 eda/iris_data.csv'

datos = pd.read_csv(filepath)


""" #QUESTION 5
plt.plot(datos.iloc[:,0],datos.iloc[:,1], marker='o')
plt.show()


#QUESTION 6
plt.hist(datos.iloc[:,2], bins=20)
ax = plt.axes()
ax.set(xlim=(0,10),xlabel='Petal length ',title="Histogram for petal length")
plt.show() """

#QUESTION 7
""" plt.hist((datos.iloc[:,0]), bins=10)
plt.hist((datos.iloc[:,1]), bins=10)
plt.hist((datos.iloc[:,2]), bins=10)
plt.hist((datos.iloc[:,3]), bins=10)
plt.show() """

##7B unanswered

#QUESTION 8
#print (datos)
#print ("COLUMNS: ", datos.columns,"\n",  sep='\n')
datos.plot.box(by='species')
#plt.show()

#QUESTION 9
#graph = sns.boxplot(x="species", y="sepal_length", data=datos)
#plt.show()

#Convertimos las columnas en filas, desdoblando estas en multinivel
stack = datos.stack()

#Sacamos la columna de especies y la desdoblamos en 4, ya que la especie será la misma en las cuatro medidas.
mySpecies = stack.loc[:, 'species'].repeat(4)

#Descartamos dicha columna ya que la ingresaremos por separado.
stack = stack.drop(labels='species', level=1)

#Ahora necesitamos sacar las medidas del multinivel. Primero obtenemos la variable multinivel, y esto lo convertimos en una serie para poder pasárselo al dataframe.
indices = stack.index
MeasureNames = indices.get_level_values(1).to_series()

SBPlot = pd.DataFrame({'species': mySpecies,
        'measurement': MeasureNames.values,
        'size':    stack.values,
                    
})

myIndexes = np.arange(0,SBPlot.shape[0],1)

SBPlot.set_index(myIndexes, inplace=True)
print(SBPlot)
#sns.boxplot(SBPlot)

#QUESTION 10
