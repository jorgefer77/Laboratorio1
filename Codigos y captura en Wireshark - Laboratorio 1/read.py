#Algoritmo para obtener el mensaje transmitido 
import sys
from scapy.all import *
from colorama import init, Fore, Style

#Se descifra el mensaje cifrado en Cesar
def descifrar_cesar(texto_cifrado, corrimiento):
    texto_descifrado = ""
    for caracter in texto_cifrado:
        if caracter.isalpha():
            nueva_posicion = ord(caracter) - corrimiento
            if caracter.islower():
                nueva_posicion = (nueva_posicion - ord('a')) % 26 + ord('a')
            else:
                nueva_posicion = (nueva_posicion - ord('A')) % 26 + ord('A')
            caracter_descifrado = chr(nueva_posicion)
        else:
            caracter_descifrado = caracter
        texto_descifrado += caracter_descifrado
    return texto_descifrado

#Se prueban los corrimientos posibles
def probar_todos_corrimientos(texto_cifrado):
    mensajes_descifrados = []
    max_ocurrencias = 0
    for corrimiento in range(26):
        texto_descifrado = descifrar_cesar(texto_cifrado, corrimiento)
        ocurrencias = sum(texto_descifrado.count(letra) for letra in "aeiouAEIOU")
        mensajes_descifrados.append((corrimiento, texto_descifrado, ocurrencias))
        max_ocurrencias = max(max_ocurrencias, ocurrencias)
    
    max_corrimiento_length = len(str(len(mensajes_descifrados) - 1))
    
    for corrimiento, mensaje, ocurrencias in mensajes_descifrados:
        espacio_numeracion = " " * (max_corrimiento_length - len(str(corrimiento)) + 5 )  
        espacio_texto = " " * (30 - len(mensaje))  
        if ocurrencias == max_ocurrencias:
            mensaje_descifrado_resaltado = Fore.GREEN + str(corrimiento) + espacio_numeracion + mensaje + Style.RESET_ALL
        else:
            mensaje_descifrado_resaltado = str(corrimiento) + espacio_numeracion + mensaje
        print(mensaje_descifrado_resaltado + espacio_texto )

#Obtiene el mensaje transmitido de la captura 
def obtener_mensaje_transmitido(captura):
    try:
        mensajes_transmitidos = []
        paquetes = rdpcap(captura)
        for pkt in paquetes:
            if Raw in pkt:
                mensaje_transmitido = pkt[Raw].load[0]
                mensajes_transmitidos.append(mensaje_transmitido)
        mensaje = bytes(mensajes_transmitidos).decode('utf-8')
        return mensaje
    except Exception as e:
        return None

if __name__ == "__main__":
    init(autoreset=True) 
    if len(sys.argv) != 2:
        sys.exit(1)
    captura = sys.argv[1]
    mensaje_transmitido = obtener_mensaje_transmitido(captura)
    if mensaje_transmitido!= None:
        probar_todos_corrimientos(mensaje_transmitido) 





