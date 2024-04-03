#Algoritmo de cifrado Cesar
import sys

#Cifrado por Cesar
def cifrar_cesar(texto, corrimiento):
    texto_cifrado =""
    for caracter in texto:
        if caracter.isalpha(): 
            ascii_inicial = ord('a') if caracter.islower() else ord('A')
            indice =(ord(caracter) -  ascii_inicial + corrimiento) % 26
            texto_cifrado += chr(ascii_inicial + indice)
        else:
            texto_cifrado += caracter

    return texto_cifrado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    texto = sys.argv[1]
    corrimiento = int(sys.argv[2])
    texto_cifrado = cifrar_cesar(texto, corrimiento)
    print(texto_cifrado)
    

    