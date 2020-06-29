import os

count = 0

file_type = raw_input("Introduce tipo de archivo a buscar:")

for (nombredir, dirs, ficheros) in os.walk('.'):
	for nombrefichero in ficheros:
		if nombrefichero.endswith(file_type):
			count = count+1
			
print(count)
			
