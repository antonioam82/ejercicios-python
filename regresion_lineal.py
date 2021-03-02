#IMPORTAMOS RECURSOS.
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#IMPORTAMOS DATOS DE MUESTRA.
boston = datasets.load_boston()
print(boston)
print("")

#TIPOS DE DATOS.
print("Información del dataset:")
print(boston.keys())
print("")

#MOSTRAR NOMBRES COLUMNAS.
print("Nombres Columnas:")
print(boston.feature_names)

#DESCRIPCIÓN COLUMNAS.
print(boston.DESCR)

#SELECCIONAR DATOS DE LA COLUMNA 5.
X = boston.data[:, np.newaxis, 5]

#EJE "y".
y = boston.target

#GRAFICAR DATOS.
plt.scatter(X, y)
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor medio")
plt.show()

#SEPARAR DATOS DE ENTRENAMIENTO DE DATOS DE PRUEBA.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#ALGORITMO DE REGRESION LINEAL.
lr = linear_model.LinearRegression()

#ENTRENAR MODELO.
lr.fit(X_train, y_train)

#OBTENER PREDICCIÓN.
Y_pred = lr.predict(X_test)

#GRAFICAR MODELO.
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title('Regresión Lineal Simple')
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

#PENDIENTE.
print("Pendiente: ",lr.coef_)
#INTERCEPTOR.
print("Interceptor: ",lr.intercept_)
print("")

#PRECISIÓN DEL MODELO.
print("Precisión del modelo: ",lr.score(X_train, y_train))
