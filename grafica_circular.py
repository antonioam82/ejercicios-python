#IMPORTAMOS "matplotlib".
import matplotlib.pyplot as plt 

#DEFINIMOS ETIQUETAS  
etiquetas = ['A', 'B', 'C', 'D', 'E', 'F'] #labels

#PORCENTAJE DE CADA PORCIÓN.
porcentas = [14,3,8,6,9,7]

#DEFIMIMOS COLORES
colores = ['#1abc9c', '#f1c40f', '#8e44ad', '#e74c3c', '#34495e', '#3498db'] #LabelColor

#DIBUJAMOS GRÁFICA.  
plt.pie(porcentas, labels = etiquetas, colors=colores,
        startangle=90, explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
        radius = 1.2, autopct = '%1.2f%%')

#TITULO
plt.title('Gráfica Circular')

#MOSTRAMOS GRÁFICA.
plt.show()
