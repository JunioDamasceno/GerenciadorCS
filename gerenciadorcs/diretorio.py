#encoding: utf-8

import pathlib
import os
import getpass

def diretorio():
    system_user = getpass.getuser()
    diretorio = pathlib.Path('/snap/gerenciadorcs/current/')
    print(diretorio)
    print(system_user)
                             
    arquivos = diretorio.glob('**/interface.glade')
    for arquivo in arquivos:
        a = "{}".format(arquivo)
        print(a)

    return(a)

teste = diretorio()
