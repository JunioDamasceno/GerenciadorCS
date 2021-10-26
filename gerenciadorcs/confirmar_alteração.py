#Este módulo recebe:
#o usuário logado no programa;
#o endereço dos arquivos binários;
#Os dados que se deseja alterar(Conta, Usuário e Senha);
#Os dados novos;
#Faz as alterações nos arquivos binários

import locale
idioma = locale.getdefaultlocale()

def confirmar_alteração(aux, ac, nu, se, asu, conta_gravada, usuario_gravado, senha_gravada, conta_nova, usuario_novo, senha_nova):

    #Cria tabelas temporárias pra armazenar os dados dos arquivos binários
    tabela_ac = []
    tabela_nu = []
    tabela_se = []
    tabela_asu = []
    arq_ac = open(ac, 'r')
    iac = 0
    for linha in arq_ac:
        linha = linha.rstrip()
        a = linha
        a = bytes.fromhex(a)
        a = a.decode('utf-8')
        tabela_ac.insert(iac, a)
        iac = iac + 1
    arq_ac.seek(0)
    arq_ac.close()

    arq_nu = open(nu, 'r')
    inu = 0
    for linha in arq_nu:
        linha = linha.rstrip()
        b = linha
        b = bytes.fromhex(b)
        b = b.decode('utf-8')
        tabela_nu.insert(inu, b)
        inu = inu + 1
    arq_nu.seek(0)
    arq_nu.close()

    arq_se = open(se, 'r')
    ise = 0
    for linha in arq_se:
        linha = linha.rstrip()
        c = linha
        c = bytes.fromhex(c)
        c = c.decode('utf-8')
        tabela_se.insert(ise, c)
        ise = ise + 1
    arq_se.seek(0)
    arq_se.close()

    arq_asu = open(asu, 'r')
    iasu = 0
    counter = 0
    for linha in arq_asu:
        linha = linha.rstrip()
        d = linha
        d = bytes.fromhex(d)
        d = d.decode('utf-8')
        tabela_asu.insert(iasu, d)
        iasu = iasu + 1
        counter = counter + 1
    arq_asu.seek(0)
    arq_asu.close()

    #armazena o usuário logado no programa
    usuario = aux
    usuario = bytes.fromhex(usuario)
    usuario = usuario.decode('utf-8')

    #Esta variável é apenas um contador para o 'while'
    c2 = 0

    #Estas tabelas armazenarão temporáriamente dados com as alterações.
    a = [] #conta
    d = [] #usuario da conta
    b = [] #senha

    #lê os dados das tabelas e altera os dados antigos,
    #armazenando-os temporariamente novas tabelas com as alterações
    while (c2 < counter):
        if (tabela_ac[c2] == conta_gravada and tabela_nu[c2] == usuario_gravado and tabela_se[c2] == senha_gravada and tabela_asu[c2] == usuario):
            a.insert(c2, conta_nova)
            d.insert(c2, usuario_novo)
            b.insert(c2, senha_nova)
        else:
            a.insert(c2, tabela_ac[c2])
            d.insert(c2, tabela_nu[c2])
            b.insert(c2, tabela_se[c2])
        c2 = c2 + 1

    #Reescreve os dados atualizados das tabelas nos arquivos binários
    arq_c = open(ac, 'w')
    arq_c.write('')
    arq_c.close()
    arq_c = open(ac, 'a+')
    for index, item in enumerate(a):
        ca = item
        ca = ca.encode('utf-8')
        ca = ca.hex()
        arq_c.write("{}\n".format(ca))
    arq_c.seek(0)
    arq_c.close()
                
    arq_n = open(nu, 'w')
    arq_n.write('')
    arq_n.close()
    arq_n = open(nu, 'a+')
    for index, item in enumerate(d):
        na = item
        na = na.encode('utf-8')
        na = na.hex()
        arq_n.write("{}\n".format(na))
    arq_n.seek(0)
    arq_n.close()

    arq_s = open(se, 'w')
    arq_s.write('')
    arq_s.close()
    arq_s = open(se, 'a+')
    for index, item in enumerate(b):
        sa = item
        sa = sa.encode('utf-8')
        sa = sa.hex()
        arq_s.write("{}\n".format(sa))
    arq_s.seek(0)
    arq_s.close()

    msg_confirmar = ''
    if idioma == ('pt_BR', 'UTF-8'):
        msg_confirmar = 'Dados alterados com sucesso'
    elif idioma == ('en_US', 'UTF-8'):
        msg_confirmar = 'Successfully changed data'
    elif idioma == ('es_ES', 'UTF-8'):
        msg_confirmar = 'Datos modificados correctamente'
    else:
        msg_confirmar = 'Successfully changed data'

    #Retorna a mensagem de dados alterados com sucesso
    return(msg_confirmar)

