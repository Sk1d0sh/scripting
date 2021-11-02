#https://www.techfacts007.in/wp-json/wp/v2/users

import sys
import requests
from bs4 import BeautifulSoup #buscador de tag en sitios web
import argparse

ordinaryParse = argparse.ArgumentParser(description="Detector de Cabeceras")
ordinaryParse.add_argument('-t','--tarjet', help='Indica un sitio web \n (https://example.com)')
ordinaryParse = ordinaryParse.parse_args()

def listas(list_wp):
    list_wp=list_wp
    for list_Rst in range(len(list_wp)):
        print('--> '+list_wp[list_Rst])
    
def versiones(peticion):
    print('-'*50)
    print('Version de Wordpress: ')
    listVersion = []
    peticion = peticion
    soup = BeautifulSoup(peticion.text,'html.parser')
    for version in soup.find_all('meta'):
        if version.get('name') == 'generator':
            v = version.get('content')
            listVersion.append(v)
    return listVersion
    

def themes(peticion):
    print('-'*50)
    print('Temas Instalados WordPress: ')
    listThemes=[]
    peticion = peticion
    soup = BeautifulSoup(peticion.text,'html.parser')
    for themes in soup.find_all('link'):
        if '/wp-content/themes' in themes.get('href'):
            href = themes.get('href')
            href = href.split('/')
            if 'themes' in href:
                posicion = href.index('themes')
                tema = href[posicion+1]
                listThemes.append(tema)
    return listThemes

def usuarios():
    pass

def plugins(peticion):
    print('-'*50)
    print('Plugins Instalados WordPress: ')
    listplugins=[]
    peticion = peticion
    soup = BeautifulSoup(peticion.text,'html.parser')
    for themes in soup.find_all('link'):
        if '/wp-content/plugins' in themes.get('href'):
            href = themes.get('href')
            href = href.split('/')
            if 'plugins' in href:
                posicion = href.index('plugins')
                plugin = href[posicion+1]
                listplugins.append(plugin)
    return listplugins

def main():
    if ordinaryParse.tarjet:
        tarjetURL = ordinaryParse.tarjet
        cabecera = {'User-Agent':'Firefox'}
        peticion = requests.get(url=tarjetURL, headers=cabecera)
        try:
            list1 = versiones(peticion)
            listas(list1)

            list1=themes(peticion)
            listas(list1)
            
            list1=plugins(peticion)
            listas(list1)

            print('-'*50)
        except:
            print("No se pudo establecer la conexion")
    else:
        print("No hay objetivo definido")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()