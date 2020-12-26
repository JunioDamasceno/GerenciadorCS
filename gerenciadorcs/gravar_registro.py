import locale
idioma = locale.getdefaultlocale()
def gravar_registro(aux, conta_name, nome_usuario, conta_ps, ac, nu, se, asu, tabela_ux):

    chave = 0
    c = 0
    print(conta_name, nome_usuario, conta_ps)
    #print(type(conta_name, nome_usuario, conta_ps))
    for linha in tabela_ux:
        if (tabela_ux[c][0] ==  conta_name and tabela_ux[c][1] == nome_usuario and tabela_ux[c][2] == conta_ps):
            chave = 1
        c = c + 1

    msg_gravar = ''
    if (chave == 1):
        if idioma == ('pt_BR', 'UTF-8'):
            msg_gravar = "Não foi possível cadastrar pois, o ítem já foi cadastrado, o sistema não aceita dados duplicados!"

        elif idioma == ('en_US', 'UTF-8'):
            msg_gravar = "It was not possible to register because the item has already been registered, the system does not accept duplicate data!"

        else:
            msg_gravar = "It was not possible to register because the item has already been registered, the system does not accept duplicate data!"
    
    else:
        #codifica os dados para armazenamento
        conta_name = conta_name.encode('utf-8')
        conta_name = conta_name.hex()
        nome_usuario = nome_usuario.encode('utf-8')
        nome_usuario = nome_usuario.hex()
        conta_ps = conta_ps.encode('utf-8')
        conta_ps = conta_ps.hex()

        #Grava os dados nos arquivos .bin
        arq_ac = open(ac, 'a+')
        arq_ac.write("{}\n".format(conta_name))
        arq_ac.seek(0)
        arq_ac.close()
        arq_nu = open(nu, 'a+')
        arq_nu.write("{}\n".format(nome_usuario))
        arq_nu.seek(0)
        arq_nu.close()
        arq_se = open(se, 'a+')
        arq_se.write("{}\n".format(conta_ps))
        arq_se.seek(0)
        arq_se.close()
        arq_asu = open(asu, 'a+')
        arq_asu.write("{}\n".format(aux))
        arq_asu.seek(0)
        arq_asu.close()

        if idioma == ('pt_BR', 'UTF-8'):
            msg_gravar = "Dados Gravados com Sucesso"

        elif idioma == ('en_US', 'UTF-8'):
            msg_gravar = "Data Saved Successfully"

        else:
            msg_gravar = "Data Saved Successfully"
        

    return(msg_gravar)
