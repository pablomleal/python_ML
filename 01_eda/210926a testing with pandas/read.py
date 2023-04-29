import pandas as pd

filepath1 = 'C:\\Users\\Usuario\\Documents\\python\\ml\\example.csv'
filepath2 = 'C:\\Users\\Usuario\\Documents\\python\\ml\\energy.json'
url = 'https://apidatos.ree.es/es/datos/generacion/estructura-generacion?start_date=2019-10-01&end_date=2021-09-01&time_trunc=month'
# data1 = pd.read_csv(filepath1)
# print (data1)

# data2 = pd.read_json(filepath2)

data3 = pd.read_json(url)