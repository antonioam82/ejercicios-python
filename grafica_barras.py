import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("CALIFICACIONES")
grupo1 = fig.add_subplot(211)
grupo2 = fig.add_subplot(212)

alums1 = ["Jorge", "Ana", "Juan", "Diana", "Pedro"]
calif1 = np.array([7.8, 5.9, 8.0, 10, 6.6])

alums2 = ["Pablo", "David", "Jose", "Carlos", "Sofia"]
calif2 = np.array([9.0, 5.0, 8.3, 7.7, 9.5])

grupo1.bar(alums1, calif1, align="center")
grupo1.set_xticks(alums1)
grupo1.set_xticklabels(alums1)
#grupo1.set_yticklabels(calif1)
grupo1.set_ylabel("CALIFICACIONES GRUPO 1")

grupo2.bar(alums2, calif2, color="g", align="center")
grupo2.set_xticks(alums2)
grupo2.set_xticklabels(alums2)
#grupo2.set_yticklabels(calif2)
grupo2.set_ylabel("CALIFICACIONES GRUPO 2")

plt.show()
