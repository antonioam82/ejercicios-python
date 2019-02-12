#CIFRADO CESAR

texto=input("Tu texto: ")

abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz0123456789" 

k=int(input("Valor de desplazamiento: "))
cifrad=""
    
for c in texto:
    if c in abc:
        cifrad += abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c

print("Texto cifrado: ",cifrad)
