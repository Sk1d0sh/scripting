import subprocess
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tarjet', help='Indica un sitio web \n (https://example.com) ')
parser = parser.parse_args()

def main():
    if parser.tarjet:
        subprocess.run("python3 /home/sk1dush/.local/lib/python3.9/site-packages/wad/__main__.py -u" + parser.tarjet + '> technologies.txt',shell=True)
        file = open("technologies.txt", 'r')
        tecnologias = file.read()
        tecnologias = tecnologias.split('[')
        tecnologias = tecnologias[1].split(']')
        tecnologias = tecnologias[0]
        tecnologias = tecnologias.split('{')
        
        for tecnologia in tecnologias:
            nuevo= tecnologia.replace('\n','')
            nuevo = nuevo.replace('            ','')
            nuevo = nuevo.replace('"','')
            nuevo = nuevo.replace(',ver:',',version:')
            nuevo = nuevo.split('}')
            nuevo = nuevo[0]
            nuevo = nuevo.replace(',','\n')
            print(nuevo)
            print("-"*50)
    else:
        print("Heeeyyy no olvides el sitio web. -h")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

        