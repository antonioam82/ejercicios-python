#IMPORTAMOS RECURSOS.
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#OBTENEMOS TEXTO DE "wikipedia".
info = wikipedia.summary("Python")
print(info)

#GENERAR NUBE
wordCloud = WordCloud().generate(info)

#MOSTRAR NUBE.
plt.imshow(wordCloud,interpolation='bilinear')
plt.axis("off")
plt.show()

image = wordCloud.to_image()
image.save("wordcloud.png")
image.show()
