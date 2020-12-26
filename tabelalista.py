def tabelalista(aux, ac, nu, se, asu):
    tabela_ac = []
    tabela_nu = []
    tabela_se = []
    tabela_asu = []
    tabela_ux = ([])
    
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
        e = linha
        e = bytes.fromhex(e)
        e = e.decode('utf-8')
        tabela_nu.insert(inu, e)
        inu = inu + 1
    arq_nu.seek(0)
    arq_nu.close()

    arq_se = open(se, 'r')
    ise = 0
    for linha in arq_se:
        linha = linha.rstrip()
        b = linha
        b = bytes.fromhex(b)
        b = b.decode('utf-8')
        tabela_se.insert(ise, b)
        ise = ise + 1
    arq_se.seek(0)
    arq_se.close()

    arq_asu = open(asu, 'r')
    iasu = 0
    counter = 0
    for linha in arq_asu:
        linha = linha.rstrip()
        c = linha
        c = bytes.fromhex(c)
        c = c.decode('utf-8')
        tabela_asu.insert(iasu, c)
        iasu = iasu + 1
        counter = counter + 1
    arq_asu.seek(0)
    arq_asu.close()

    usuario = aux
    usuario = bytes.fromhex(usuario)
    usuario = usuario.decode('utf-8')
    c2 = 0
    c3 = 0

    while (c2 < counter):
        d = tabela_asu[c2]
        if (d == usuario):
            tabela_ux.insert(c3, (tabela_ac[c2], tabela_nu[c2], tabela_se[c2]))
            c3 = c3 + 1
        c2 = c2 + 1

    tabela_ux.sort()
    return(tabela_ux)
