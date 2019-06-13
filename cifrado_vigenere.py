
LETTERS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def main():
    myMessage=input("Mensaje: ")
    myKey='MINOMBREESANTONIOALFONSO'
    myMode=input("Mode: ")

    if myMode=='encrypt':
        translated=encryptMessage(myKey,myMessage)
    elif myMode=='decrypt':
        translated=decryptMessage(myKey,myMessage)
    print(translated)

def encryptMessage(key,message):
    return translateMessage(key,message,'encrypt')

def decryptMessage(key,message):
    return translateMessage(key,message,'decrypt')

def translateMessage(key,message,mode):
    translated=[]
    keyIndex=0
    key=key.upper()

    for symbol in message:
        num=LETTERS.find(symbol.upper())
        if num!=-1:
            if mode=='encrypt':
                num+=LETTERS.find(key[keyIndex])
            elif mode=='decrypt':
                num-=LETTERS.find(key[keyIndex])
            num%=len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex+=1
            if keyIndex==len(key):
                keyIndex=0

        else:
            translated.append(symbol)
    return ('').join(translated)

if __name__ == '__main__':
    main()
