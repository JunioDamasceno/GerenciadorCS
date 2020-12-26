#encoding: utf-8

import pathlib
import os
import getpass
import locale

def diretorio():
    idioma = locale.getdefaultlocale()
    print(idioma)
    diretorio = pathlib.Path('/snap/gerenciadorcs/current/')
    print(diretorio)
    arquivos = ''
    a = ''

    if idioma == ('pt_BR', 'UTF-8'):
        print('The Language of the system is Portugese of Brazil')
        arquivos = diretorio.glob('**/interface-pt-BR.glade')

    elif idioma == ('en_US', 'UTF-8'):
        print('The language of the system is English USA')
        arquivos = diretorio.glob('**/interface-en-US.glade')
    else:
        arquivos = diretorio.glob('**/interface-en-US.glade')

    for arquivo in arquivos:
        a = "{}".format(arquivo)
        print(a)

    return(a)

teste = diretorio()
