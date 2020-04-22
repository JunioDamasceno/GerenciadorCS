#!/usr/bin/python
import gi
gi.require_version('Gtk', "3.0")
from gi.repository import Gtk

class main_window:
    
    def __init__(self):

        #Indica que a interface, menus, janelas, módulos e caixas de diálogo
        #do programa serão carregadas a partir do conjunto de instruções contidos
        #no arquivo 'interface.glade'. Este arquivo foi criado no programa
        #Glade versão 3.22.1, o Glade é um construtor de interfaces de usuário
        #para GTK+ e GNOME.
        self.gladefile = '${SNAP}/current/glade/interface.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        
        self.builder.connect_signals(self)

        #Ativa cada janela/tela e/ou módulo que compõe o programa,
        #estas definições estão contidas no arquivo 'interface.glade'
        self.main_window = self.builder.get_object('main_window')
        self.main_window.show()
        self.login = self.builder.get_object("login")
        self.new_user = self.builder.get_object("new_user")
        self.menu = self.builder.get_object('menu')
        self.cadastrar = self.builder.get_object('cadastrar')
        self.exibir = self.builder.get_object('exibir')
        self.alterar = self.builder.get_object('alterar')
        self.lista = self.builder.get_object('lista')
        self.grid = self.builder.get_object('grid')
        self.dialogo_sobre = self.builder.get_object('dialogo_sobre')
        self.barra_menu = self.builder.get_object('barra_menu')

        #Esta variável serve para armazenar qual usuário está logado,
        #controla quais informações ele irá armazenar e quais informações ele
        #pode acessar.
        self.aux = ""

        #A função 'dialogo' é chamada apenas para exibir uma caixa de
        #diálogo na tela que exibe uma mensagem para o usuário.
        def dialogo(a):
            self.dialogo = self.builder.get_object('dialogo')
            self.rotulo = self.builder.get_object('rotulo')
            self.dialogo.show()
            mensagem = a
            self.rotulo.set_label(mensagem)
            response = self.dialogo.run()
            if response == Gtk.ResponseType.OK:
                self.dialogo.hide()
            if response == Gtk.ResponseType.DELETE_EVENT:
                self.dialogo.close()
            return response

        #Estas variáveis serão utilizadas no momento de exibir dados que
        #o usuário armazenou no banco de dados
        self.tabela_ux = ([])
        self.lista = ""

        #Esta variável serve apenas pra chamar a função 'dialogo' dentro de
        #outras funções.
        self.dialogo_c = dialogo

        #Estas variáveis funcionam como chaves que operam 'While' e 'if'
        #na janela de 'login'
        self.chave = 1
        self.chave_nuser = 1
        self.chave_check = 2

        #As duas variáveis abaixo funcionam como chaves para verificar
        #se usuário e senha estão corretos, na janela de 'login'.
        cux = -1
        csx = 0

        #Estas variáveis são apenas contadores, por exemplo, iux = iux + 1.
        iux = 0
        isx = 0
                
        while (self.chave == 1):
            #Ativa os campos para inserir usuário e senha
            self.msg_aux = self.builder.get_object('msg_aux')
            self.msg_pux = self.builder.get_object('msg_pux')
            #Exibe na tela a janela de 'login'
            self.login.show()
            #Armazena respostas que o usuário envia a partir da janela
            #de 'login', por exemplo, 'OK', "Fechar", "Aplicar"
            response = self.login.run()
            
            #Se o usuário clicar no 'botão OK', enviará para a variável 'response'
            #o resultado equivalente a OK (é um número definido pela biblioteca
            #Gtk que representa OK, só pra constar), se esta condição for
            #verdadeira, ele executa o conjunto de instruções abaixo. Basicamente
            #ele armazena usuário e senha digitados nos campos em duas variáveis
            #e verifica se a combinação e verdadeira no banco de dados de usuário
            #e de senha.
            if (response == Gtk.ResponseType.OK):
                aux = self.msg_aux.get_text()
                aux = aux.encode('utf-8')
                aux = aux.hex()
                pux = self.msg_pux.get_text()
                pux = pux.encode('utf-8')
                pux = pux.hex()
                arq_ux = open('ux.bin', 'r')
                arq_sx = open('sx.bin', 'r')
                
                for linha in arq_ux:
                    linha = linha.rstrip()
                    iux = iux + 1
                    if (linha == aux):
                        cux = iux
                arq_ux.seek(0)
                arq_ux.close()
                
                for linha in arq_sx:
                    linha = linha.rstrip()
                    isx = isx + 1
                    if (linha == pux):
                        if (csx < cux):
                            csx = isx
                arq_sx.seek(0)
                arq_sx.close()

                #Se usuário e senha digitados existirem no banco de dados de
                #usuário e de senha e forem correspondentes ele executa o conjunto
                #de instruções abaixo: Abre caixa de diálogo e exibe a mensagem
                #armazenada em 'mlogin1', quando o usuário fechar a caixa de
                #diálogo clicando em 'OK' ou em 'sair' ele fecha janela de 'login'
                #e finaliza o 'while' mudando o valor de 'chave' para 0.
                #Caso usuário e senha digitados não existam no banco dedados de
                #usuário e de senha correspondentes ele abre a caixa de diálogo
                #e mostra a mensagem armazenada em 'mlogin2'. A condição de 'while'
                #não foi atendida, portanto ele volta ao início do 'while'.
                if (cux == csx):
                    print("senha correta!")
                    mlogin1 = "senha correta, login efetuado com sucesso!"
                    dialogo(mlogin1)
                    self.login.hide()
                    self.aux = aux #armazena o nome do usuário logado em 'self.aux'
                    self.chave = 0
                else:
                    print("senha incorreta!")
                    mlogin2 = "Usuário e/ou senha incorretas!"
                    dialogo(mlogin2)                    

            #Se o usuário clicar no botão "fechar ou no botão "sair" no topo
            #direito da janela de login ele fecha a janela de login e a
            #janela principal do programa, finalizando a execução como um todo.
            #Há uma duas funções 'on_login_destroy' e 'on_main_window_destroy'
            #que estão no final do código que complementam este comando.
            #Estas funções também foram definidas no arquivo 'interface.glade'.
            if response == Gtk.ResponseType.DELETE_EVENT:
                self.login.close()
                self.main_window.close()
                self.chave = 0

            #Se o usuário clicar no botão 'cadastrar novo usuário' ele executa
            #o conjunto de instruções abaixo, pois a variável 'response' recebe
            #o valor de 'aceitar'
            if response == Gtk.ResponseType.ACCEPT:
                #Estas variáveis são chaves utilizadas para verificar se o nome
                #de usuário que se quer cadastrar já existe ou não no sistema.
                ad = 0
                nuser = 0

                while(self.chave_nuser == 1):
                    #Habilita os campos pra criar novo usuário e senha
                    #Exibe a caixa de dialogo "new_user"
                    self.user_name = self.builder.get_object("user_name")
                    self.user_p = self.builder.get_object("user_p")
                    self.new_user.show()
                    #Esta variável armazena a resposta que o usuario envia
                    #na caixa de diálogo 'new_user'
                    response3 = self.new_user.run()
                    #Se a resposta for 'OK' ele executa as instruções abaixo
                    if response3 == Gtk.ResponseType.OK:
                        #Armazena os valores digitados nos campos de
                        #'Nome de usuário' e de 'senha' e verifica se o usuário
                        #existe ou não no banco de dados de usuário
                        nuser = self.user_name.get_text()
                        nuser = nuser.encode('utf-8')
                        nuser = nuser.hex()
                        userp = self.user_p.get_text()
                        userp = userp.encode('utf-8')
                        userp = userp.hex()
                        #Serve para impedir que o usuário tente cadastrar um
                        #usuário sem senha, ou uma senha sem nome de usuário
                        #Se os dois campos tiverem preenchidos ele verifica se
                        #o nome do usuário já existe no banco de dados
                        if (nuser == "" or userp == ""):
                            mnuser1 = ('você não pode deixar campos em branco')
                            dialogo(mnuser1)
                            ad = nuser
                        else:
                            user_check = open('ux.bin', 'r')
                            for linha in user_check:
                                linha = linha.rstrip()
                                #a variável ad armazena cada linha do arquivo uma por vez
                                ad = linha
                                #Se o valor contido em alguma linha corresponder ao
                                #ao nome do usuário o valor de 'self.chave_check' será 1
                                if (ad == nuser):
                                    self.chave_check = 1
                            user_check.seek(0)
                            user_check.close()
                            
                    #Se o usuário clicar em 'cancelar' na caixa de diálogo 'new_user'
                    if response3 == Gtk.ResponseType.CANCEL:
                        self.user_name.set_text("")
                        self.user_p.set_text("")
                        self.new_user.hide()
                        self.chave_check = 2
                        self.chave_nuser = 0

                    #Se o usuário já existir a variável 'chave_check assume o valor 1,
                    #e exibe a caixa de diálogo com a mensagem contida em 'mnuser2',
                    #Zera o valor armazenado nos campos Nome do usuário e Senha
                    #e o 'While' retorna ao início pois a condição não foi satisfeita.
                    if (self.chave_check == 1):
                        mnuser2 = "Nome de usuário já cadastrado, tente outro nome"
                        dialogo(mnuser2)
                        ad = 0
                        nuser = 0
                    #A variável ad serve apenas para verificar se o Nome de usuário
                    #existe ou não no banco de dados, se não existir o valor da
                    #variável 'self.chave_check' será 0.
                    if (ad != nuser):
                        self.chave_check = 0

                    #Se o valor de 'self.chave_check' for 0 ele executa as instruções
                    #abaixo, que basicamente é: armazenar o nome de usuário e senha
                    #do novo usuário no banco de dados, exibir a caixa de diálogo
                    #com a mensagem contida em 'mnuser3', assim que o usuário fechar
                    #a caixa de diálogo ele fecha a caixa de diálogo 'new_user' e
                    # volta a janela de 'login'.
                    if (self.chave_check == 0):
                        arq_ux = open('ux.bin', 'a+')
                        arq_sx = open('sx.bin', 'a+')
                        arq_ux.write("{}\n".format(nuser))
                        arq_sx.write("{}\n".format(userp))
                        arq_ux.seek(0)
                        arq_sx.seek(0)
                        arq_ux.close()
                        arq_sx.close()
                        mnuser3 = "usuário cadastrado com sucesso, faça login para acessar o programa"
                        dialogo(mnuser3)
                        self.new_user.hide()
                        self.new_user.close()
                        self.chave_nuser = 0
                        
                
        #Se usuário e senha estiverem corretos ele exibe o 'menu' do sistema.              
        if (cux == csx):
            self.menu.show()
            
    #Fecha o programa por completo se o usuário clicar no botão 'sair' na
    #janela principal 'main_window'.
    def on_main_window_destroy(self, object, data=None):
        print("quit with cancel")
        Gtk.main_quit()
        
    #Fecha o programa por completo se o usuário clicar no botão 'fechar' ou
    #no botão 'sair' na janela de 'login'
    def on_login_destroy(self, object, data=None):
        print("login quit with cancel")
        Gtk.main_quit()

    def on_menu_sair_activate(self, object, data=None):
        print("quit with menu-arquivo-sair")
        self.main_window.close()
        Gtk.main_quit()

    def on_menu_ajuda_sobre_activate(self, object, data=None):
        self.dialogo_sobre.show()
        response = self.dialogo_sobre.run()
        if (response == Gtk.ResponseType.OK):
            self.dialogo_sobre.hide()
        if (response == Gtk.ResponseType.DELETE_EVENT):
            self.dialogo_sobre.hide()
        
        
    #Com o usuário logado e o 'menu' visível se o usuário clicar no botão
    #'cadastar' ele esconde o 'menu' e abre o módulo 'Cadastrar uma nova senha'
    def on_botao_cadastrar_clicked(self, object, data=None):
        self.menu.hide()
        self.cadastrar.show()
        
    #Esta função grava a conta e a senha que o usuário deseja armazenar
    def on_botao_gravar_registro_clicked(self, object, data=None):
        self.conta_name = self.builder.get_object('conta_name')
        self.nome_usuario = self.builder.get_object('nome_usuario')
        self.conta_ps = self.builder.get_object('conta_ps')
        
        conta_name = self.conta_name.get_text()
        nome_usuario = self.nome_usuario.get_text()
        conta_ps = self.conta_ps.get_text()
        conta_name = conta_name.encode('utf-8')
        conta_name = conta_name.hex()
        nome_usuario = nome_usuario.encode('utf-8')
        nome_usuario = nome_usuario.hex()
        conta_ps = conta_ps.encode('utf-8')
        conta_ps = conta_ps.hex()

        arq_ac = open('ac.bin', 'a+')
        arq_ac.write("{}\n".format(conta_name))
        arq_ac.seek(0)
        arq_ac.close()
        arq_nu = open('nu.bin', 'a+')
        arq_nu.write("{}\n".format(nome_usuario))
        arq_nu.seek(0)
        arq_nu.close()
        arq_se = open('se.bin', 'a+')
        arq_se.write("{}\n".format(conta_ps))
        arq_se.seek(0)
        arq_se.close()
        arq_asu = open('asu.bin', 'a+')
        arq_asu.write("{}\n".format(self.aux))
        arq_asu.seek(0)
        arq_asu.close()
        msg_gravar = "Dados Gravados com Sucesso"
        self.dialogo_c(msg_gravar)
        self.conta_name = self.conta_name.set_text("")
        self.nome_usuario = self.nome_usuario.set_text("")
        self.conta_ps = self.conta_ps.set_text("")

    #volta para o menu principal, este botão está no módulo 'cadastrar'
    def on_botao_voltarc_clicked(self, objetc, data=None):
        self.cadastrar.hide()
        self.menu.show()
        
    #Com o usuário logado e o 'menu' visível se o usuário clicar no botão
    #'exibir' ele esconde o menu e abre o módulo 'Exibir senhas cadastradas'
    def on_botao_exibir_clicked(self, object, data=None):
        self.menu.hide()
        self.exibir.show()
        tabela_ac = []
        tabela_nu = []
        tabela_se = []
        tabela_asu = []
        

        arq_ac = open('ac.bin', 'r')
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

        arq_nu = open('nu.bin', 'r')
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

        arq_se = open('se.bin', 'r')
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

        arq_asu = open('asu.bin', 'r')
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

        usuario = self.aux
        usuario = bytes.fromhex(usuario)
        usuario = usuario.decode('utf-8')
        c2 = 0
        c3 = 0

        while (c2 < counter):
            d = tabela_asu[c2]
            if (d == usuario):
                self.tabela_ux.insert(c3, (tabela_ac[c2], tabela_nu[c2], tabela_se[c2]))
                c3 = c3 + 1
            c2 = c2 + 1

        self.lista = Gtk.ListStore(str, str, str)
        for software_ref in self.tabela_ux:
            self.lista.append(list(software_ref))

        self.current_filter_language = None

        self.language_filter = self.lista.filter_new()
        
        treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["Conta", "Usuário", "Senha"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            treeview.append_column(column)

        scrollable_treelist = Gtk.ScrolledWindow()
        scrollable_treelist.set_vexpand(True)
        self.grid.attach(scrollable_treelist, 0, 0, 8, 10)

        scrollable_treelist.add(treeview)

        self.grid.show_all()
        
    #volta para o menu principal, este botão está no módulo 'exibir'
    def on_botao_voltare_clicked(self, object, data=None):
        self.tabela_ux = ([])
        self.lista.clear()
        self.exibir.hide()
        self.menu.show()
        
    #Com o usuário logado e o 'menu' visível se o usuário clicar no botão
    #'alterar' ele esconde o menu e abre o módulo 'Alterar uma conta ou senha cadastrada'
    def on_botao_alterar_clicked(self, object, data=None):
        self.menu.hide()
        self.alterar.show()

    #verifica se a conta e senha que o usuário deseja alterar existe no banco
    #de dados do sistema, se existir ele faz a alteração, caso contrário ele
    #retorna que a conta que o usuário deseja cadastrar não existe.
    def on_botao_confirmar_alteracao_clicked(self, object, data=None):
        self.conta_gravada = self.builder.get_object('conta_gravada')
        self.usuario_gravado = self.builder.get_object('usuario_gravado')
        self.senha_gravada = self.builder.get_object('senha_gravada')
        self.conta_nova = self.builder.get_object('conta_nova')
        self.usuario_novo = self.builder.get_object('usuario_novo')
        self.senha_nova = self.builder.get_object('senha_nova')
        conta_gravada = self.conta_gravada.get_text()
        usuario_gravado = self.usuario_gravado.get_text()
        senha_gravada = self.senha_gravada.get_text()
        conta_nova = self.conta_nova.get_text()
        usuario_novo = self.usuario_novo.get_text()
        senha_nova = self.senha_nova.get_text()

        #Se o usuário não tiver a intenção de renomear a conta ele pode deixar
        #o campo segundo campo'nome da conta' em branco que o sistema utilizará
        #o mesmo nome da conta atual e irá alterar apenas a senha se a conta
        #existir.
        if (conta_nova == ""):
            conta_nova = conta_gravada
        if (usuario_novo == ""):
            usuario_novo = usuario_gravado

        if (senha_nova == ""):
            msg_senha_vazia = 'Você não pode cadastrar uma senha em branco'
            self.dialogo_c(msg_senha_vazia)
            self.conta_gravada = self.conta_gravada.set_text("")
            self.usuario_gravado = self.usuario_gravado.set_text("")
            self.senha_gravada = self.senha_gravada.set_text("")
            self.conta_nova = self.conta_nova.set_text("")
            self.usuario_novo = self.usuario_novo.set_text("")
            self.senha_nova = self.senha_nova.set_text("")
        else:
            #Os dados do banco de dados serão temporáriamente armazenados em
            #listas e/ou tuples para manipulação e verificação interna antes de
            #fazer as alterações nos 'arquivos' banco de dados.
            tabela_ac = []
            tabela_nu = []
            tabela_se = []
            tabela_asu = []
            arq_ac = open('ac.bin', 'r')
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

            arq_nu = open('nu.bin', 'r')
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

            arq_se = open('se.bin', 'r')
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

            arq_asu = open('asu.bin', 'r')
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

            usuario = self.aux
            usuario = bytes.fromhex(usuario)
            usuario = usuario.decode('utf-8')

            #Esta variável é apenas um contador para o 'while'
            c2 = 0

            #Estas tabelas armazenarão temporáriamente dados com as alterações.
            a = [] #conta
            d = [] #usuario da conta
            b = [] #senha
            c = [] #usuario do gerenciador

            #esta chave serve como parametro de condições dentro do 'if' se ela for
            #maior que zero, significa que existe pelo menos uma combinação de
            #conta, senha e usuário, portanto ela faz a alteração nesta conta, se
            #houver mais de uma conta com a mesma senha, pertencente ao mesmo usuário
            #ele faz a alteração em todas, o sistema permite que o usuário cadastre
            #duas ou mais contas e senhas iguais pro mesmo usuário, optei por deixar isso
            #livre para o usuário escolher.
            chave_alterar = 0
            while (c2 < counter):
                if (tabela_ac[c2] == conta_gravada and tabela_nu[c2] == usuario_gravado and tabela_se[c2] == senha_gravada and tabela_asu[c2] == usuario):
                    a.insert(c2, conta_nova)
                    d.insert(c2, usuario_novo)
                    b.insert(c2, senha_nova)
                    chave_alterar = chave_alterar + 1
                else:
                    a.insert(c2, tabela_ac[c2])
                    d.insert(c2, tabela_nu[c2])
                    b.insert(c2, tabela_se[c2])
                c2 = c2 + 1

            if (chave_alterar > 0):
                arq_c = open('ac.bin', 'w')
                arq_c.write('')
                arq_c.close()
                arq_c = open('ac.bin', 'a+')
                for index, item in enumerate(a):
                    ca = item
                    ca = ca.encode('utf-8')
                    ca = ca.hex()
                    arq_c.write("{}\n".format(ca))
                arq_c.close()
                
                arq_n = open('nu.bin', 'w')
                arq_n.write('')
                arq_n.close()
                arq_n = open('nu.bin', 'a+')
                for index, item in enumerate(d):
                    na = item
                    na = na.encode('utf-8')
                    na = na.hex()
                    arq_n.write("{}\n".format(na))
                arq_n.close()

                arq_s = open('se.bin', 'w')
                arq_s.write('')
                arq_s.close()
                arq_s = open('se.bin', 'a+')
                
                for index, item in enumerate(b):
                    sa = item
                    sa = sa.encode('utf-8')
                    sa = sa.hex()
                    arq_s.write("{}\n".format(sa))
                arq_s.close()

                msg_alterar_s = 'Dados alterados com sucesso'
                self.dialogo_c(msg_alterar_s)
                self.conta_gravada = self.conta_gravada.set_text("")
                self.usuario_gravado = self.usuario_gravado.set_text("")
                self.senha_gravada = self.senha_gravada.set_text("")
                self.conta_nova = self.conta_nova.set_text("")
                self.usuario_novo = self.usuario_novo.set_text("")
                self.senha_nova = self.senha_nova.set_text("")
                chave_alterar = 0
            else:
                msg_alterar_e = 'A conta e senha que você deseja altarar não está cadastrada'
                self.dialogo_c(msg_alterar_e)
                self.conta_gravada = self.conta_gravada.set_text("")
                self.usuario_gravado = self.usuario_gravado.set_text("")
                self.senha_gravada = self.senha_gravada.set_text("")
                self.conta_nova = self.conta_nova.set_text("")
                self.usuario_novo = self.usuario_novo.set_text("")
                self.senha_nova = self.senha_nova.set_text("")
                chave_alterar = 0

            #volta para o menu principal, este botão está no módulo 'alterar'
    def on_botao_voltara_clicked(self, object, data=None):
        self.alterar.hide()
        self.menu.show()
        
if __name__ == "__main__":
    main = main_window()
    Gtk.main()
