#REVERSE CIPHER
from VALID import ns

while True:
	text = raw_input("Your text: ")
	translated = ""
	i = len(text) - 1
	
	while i >= 0:
		translated = translated + text[i]
		i = i - 1
		print(translated)
		
	print('Final translation: ',translated)
	
	conti = ns(raw_input("Continue(n/s)?: "))
	if conti == "n":
		break
