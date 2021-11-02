import sys
import argparse
import os

ordinaryParse = argparse.ArgumentParser(description='Filtrado de NMAP')
ordinaryParse.add_argument('-p','--path', help='Indica la ruta del archivo NMAP')
ordinaryParse = ordinaryParse.parse_args()

def main():
    if ordinaryParse.path:
        pathfileFilter = ordinaryParse.path
        filterOne = '/'
        filterTwo = 'Nmap scan report for'
        listPort= []
        listHost=""
        with open(pathfileFilter, 'r') as fileFilter:
            for line in fileFilter:
                if filterOne in line:
                    listPort.append(line)
                if filterTwo in line:
                    listHost= line
        print(listHost)
        print('-'*50)
        host=listHost.split(filterTwo)
        ports= ""
        for filterNumber in listPort:
            x = filterNumber.split(filterOne)
            ports = ports+x[0]+','

        print(f'Host:-->{host[1][:-1]}')
        print(f'Puertos:--> {ports[:-1]}')
        print(f'sudo nmap -sC -sV -p{ports[:-1]}{host[1][:-1]} -oN nmapVersion.txt')
        print('-'*50)
    else:
        print('No se encontro archivo')
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()