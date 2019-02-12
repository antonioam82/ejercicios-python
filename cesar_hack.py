#USO DE "fuerza bruta" PARA DESCIFRAR CIFRADO CESAR. 
texto=input("Mensaje: ")

caracts='ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz0123456789'

for key in range(len(caracts)):
    traducido=''

    for elem in texto:
        if elem in caracts:
            elemIndex=caracts.find(elem)
            tradIndex=elemIndex-key

            if tradIndex<0:
                tradIndex=tradIndex+len(caracts)
            traducido=traducido+caracts[tradIndex]
        else:
            traducido=traducido+elem

        if len(traducido)==len(texto):
            print('key #%s: %s' % (key, traducido))




