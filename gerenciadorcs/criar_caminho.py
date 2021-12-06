#!/usr/bin/python
# encoding: utf-8

import os
import getpass

def verificar_arquivos():
    usuario = getpass.getuser()
    caminho = '/home/' + usuario + '/snap/gerenciadorcs/current/bin'
    arquivo_ac = caminho + '/ac.bin'
    arquivo_asu = caminho + '/asu.bin'
    arquivo_nu = caminho + '/nu.bin'
    arquivo_se = caminho + '/se.bin'
    arquivo_sx = caminho + '/sx.bin'
    arquivo_ux = caminho + '/ux.bin'

    counter_caminho = 0
    counter_arquivos = 0

    if not os.path.exists(caminho):
        os.makedirs(caminho)
        counter_caminho = counter_caminho + 1

    if not os.path.exists(arquivo_ac):
        open(arquivo_ac, 'w')
        counter_arquivos = counter_arquivos + 1

    if not os.path.exists(arquivo_asu):
        open(arquivo_asu, 'w')
        counter_arquivos = counter_arquivos + 1

    if not os.path.exists(arquivo_nu):
        open(arquivo_nu, 'w')
        counter_arquivos = counter_arquivos + 1

    if not os.path.exists(arquivo_se):
        open(arquivo_se, 'w')
        counter_arquivos = counter_arquivos + 1

    if not os.path.exists(arquivo_sx):
        open(arquivo_sx, 'w')
        counter_arquivos = counter_arquivos + 1

    if not os.path.exists(arquivo_ux):
        open(arquivo_ux, 'w')
        counter_arquivos = counter_arquivos + 1

    if (counter_caminho == 1 and counter_arquivos == 6):
        print('os arquivos necessários foram criados')

    else:
        print('os arquivos necessários não foram criados, pois já existem')
        
verificar_arquivos()
