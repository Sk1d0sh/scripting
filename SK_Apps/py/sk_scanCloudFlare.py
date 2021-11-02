import requests
import argparse
import sys

ordinaryParse = argparse.ArgumentParser(description="Detector de CloudFlare") 
ordinaryParse.add_argument('-t', '--tarjet', help='Indica un sitio web \n (https://example.com)')
ordinaryParse = ordinaryParse.parse_args()

def main():
    if ordinaryParse.tarjet:
        try:
        # https://hunter.io example cloudflare
            website = ordinaryParse.tarjet
            palabra = "cloudflare"
            url = requests.get(website)
            cabeceras = dict(url.headers)
            verificacion = False
            for cabecera in cabeceras:
                if palabra in cabeceras[cabecera].lower():
                    verificacion = True
                    break

            if verificacion == True:
                print(f"Sitio tiene CloudFlare. Cabecera:: \n--> {cabeceras[cabecera]}")
            else:
                print("Na nay")
        except:
            print("No se pudo establecer la conexion")
    else:
        print("No hay objetivo definido")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()