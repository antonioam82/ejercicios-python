# Importar librerias necesarias de Python
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr

# Activamos la conversión automática entre pandas y R
pandas2ri.activate()

# Importamos las librerías necesarias de R
base = importr('base')
ggplot2 = importr('ggplot2')
stats = importr('stats')

# Cargamos un conjunto de datos de ejemplo en R
robjects.r('data(mtcars)')

# Definimos el modelo lineal en R
robjects.r('''
linear_model <- lm(mpg ~ wt, data = mtcars)
''')

# Obtenemos un resumen del modelo
summary = robjects.r('summary(linear_model)')

# Convertimos el objeto R resultante en un DataFrame de pandas
summary_df = pandas2ri.rpy2py(summary)

# Imprimimos el resumen del modelo
print(summary_df)

# Hacemos un gráfico de dispersión con la línea de regresión
robjects.r('''
scatter_plot <- ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  geom_smooth(method = 'lm', se = FALSE) +
  labs(title = 'Scatter Plot with Linear Regression')
''')

# Mostramos el gráfico
robjects.r('print(scatter_plot)')
