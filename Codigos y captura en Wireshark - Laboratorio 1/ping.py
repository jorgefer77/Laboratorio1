#Algoritmo para enviar los caracteres del texto cifrado en varios paquetes ICMP
import sys
import random
import time
from scapy.all import *

#Genera una secuencia aleatoria (entre 0x10 y 0x37 incluyendo ambos) 
def generar_secuencia_aleatoria():
    valores = random.sample(range(0x10, 0x38), 40 )
    return bytes(valores)  
 
#Se envian los caracteres en paquetes ICMP
def enviar_caracteres_icmp(texto):
    ip_origen = "10.0.2.15"
    secuencia = 1
    for i, caracter in enumerate(texto):
        secuencia_aleatoria = generar_secuencia_aleatoria()
        payload = caracter.encode() + b'*#' +  b"\x00" * 5 + secuencia_aleatoria 
        id_paquete = i + 1
        paquete = IP(src=ip_origen, dst="127.0.0.1", ttl=64) / ICMP(type=8, id=id_paquete, seq=secuencia) / Raw(load=payload)
        secuencia += 1
        send(paquete)
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    texto = sys.argv[1]
    enviar_caracteres_icmp(texto)














