# -*- coding: utf-8 -*-
"""T2-1-Correlacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VZg_0GNXqj6hgFC0XXJ7ahcRS1SkhddF
"""

import pandas as pd

#Para leer el CSV
data_ads = pd.read_csv("/content/Advertising.csv")
#()  {}

data_ads.head()
#Data set que evidecia los gastos que se tiene en TV , Radio , Newspaper y como eso repercute en las ventas

len(data_ads)

#Biblioteca de python para trabajar con vectores y matrices
import numpy as np

#Numerador de coeficiente de correlacion de pearson entre la TV y Sales
#data_ads["corrn"] es el numerador de coeficiente de correlacion de pearson
data_ads["corrn"] = (data_ads["TV"]-np.mean(data_ads["TV"]))*(data_ads["Sales"] - np.mean(data_ads["Sales"]))

data_ads.head()

#Sumatoria 1
x1 = (data_ads["TV"]-np.mean(data_ads["TV"]))**2

#Sumatoria 2

x2 = (data_ads["Sales"]-np.mean(data_ads["Sales"]))**2


#Calculo del coeficiente de correlacion de pearson

Cp = sum(data_ads["corrn"])/ np.sqrt(sum(x1)*sum(x2))

print('El coeficiente de correlacion de pearson es {}'.format(Cp))

#Ahora esto vamos a convertirlo en una funcion donde solo vamos a ingresar el dataframe
#y los campos a evaluar la correlacion

def correlacion(data_frame,campo1,campo2):
  data_frame["corrn"] = (data_frame[campo1]-np.mean(data_frame[campo1]))*(data_frame[campo2] - np.mean(data_frame[campo2]))
    #Sumatoria 1
  x1 = (data_frame[campo1]-np.mean(data_frame[campo1]))**2
  #Sumatoria 2
  x2 = (data_ads[campo2]-np.mean(data_ads[campo2]))**2
  #Calculo del coeficiente de correlacion de pearson
  Cp = sum(data_frame["corrn"])/ np.sqrt(sum(x1)*sum(x2))
  return Cp

#()  {}
print('La correlacion de los gastos de tv y las ventas son {}'.format(correlacion(data_ads,"TV","Sales")))

print(type(correlacion(data_ads,"TV","Sales")))

#()  {}
print('La correlacion de los gastos de Radio y las ventas son {}'.format(correlacion(data_ads,"Radio","Sales")))

cols = data_ads.columns.values
cols

#Vamos a eliminar las columnas que se adiciono que ahora data
data_ads = data_ads.drop('corrn',axis=1)
print(data_ads)

cols = data_ads.columns.values
cols

#Con esto estamos hallando la correlacion de todas contra todas las variables.
for x in cols:
  for y in cols:
    print(x + " , " + y + " : " + str(correlacion(data_ads,x,y)))

#Según lo que se puede apreciar lo que más aumenta las ventas son la publicidad por TV

import matplotlib.pyplot as plt

#vamosa ver la tendencia que se tiene entre la tv y las ventas
#()  {}
plt.plot(data_ads["TV"] ,  data_ads["Sales"] , "ro")
plt.title("Gasto en TV vs Ventas del Producto")

#vamosa ver la tendencia que se tiene entre la Radio y las ventas
#()  {}
plt.plot(data_ads["Radio"] ,  data_ads["Sales"] , "go")
plt.title("Gasto en Radio vs Ventas del Producto")

cols

#vamosa ver la tendencia que se tiene entre la Newspaper y las ventas
#()  {}
plt.plot(data_ads["Newspaper"] ,  data_ads["Sales"] , "bo")
plt.title("Gasto en Periodico vs Ventas del Producto")

"""## Uso de la Funcion .corr() para poder hallar la correlacion en usando pandas"""

#Ahora en pandas nosotros tenemos una funcion para hallar la matriz de correlacion con un solo comando
#Para leer el CSV
#()  {}
data_ads = pd.read_csv("/content/Advertising.csv")
data_ads.corr()

plt.matshow(data_ads.corr())



