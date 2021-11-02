# Previene ClicHackihn
# X-Frame-Options : SAMEORIGIN or Deny ---> Recomendado
# (-)*50
# Previene Cors Site Scripting
# X-XSS-Protection : 1; mode=block ---> Recomendado
# (-)*50
# Previene Incompatibilidades relacionadas con Type
# X-Content-Type-Options : nosniff or ss
# (-)*50
# Content-Security-Policy:  
# (-)*50
# Fuerza conexiones HTTPS
# Strict-transport-Security
# (-)*50


import requests
import argparse
import sys

ordinaryParse = argparse.ArgumentParser(description="Detector de Cabeceras")
ordinaryParse.add_argument('-t','--tarjet', help='Indica un sitio web \n (https://example.com)')
ordinaryParse = ordinaryParse.parse_args()

def main():
    if ordinaryParse.tarjet:
        try:
            url = requests.get(url=ordinaryParse.tarjet)
            cabeceras = dict(url.headers)
            for cabecera in cabeceras:
                print(cabecera+" : "+cabeceras[cabecera])

        except:
            print("No se pudo establecer la conexion")
    else:
        print("No hay objetivo definido")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()