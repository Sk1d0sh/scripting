import sys
import requests 

def main():
    url = 'http://10.10.199.153/wp-login.php'
    tarjetURL = url
    cabecera = {'User-Agent':'Firefox'}
    peticion = requests.post(url=tarjetURL, headers=cabecera)

    print(peticion)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()