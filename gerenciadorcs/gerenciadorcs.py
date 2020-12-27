#!/usr/bin/python
# encoding: utf-8

#Este módulo verifica os arquivos binários.
from criar_caminho import verificar_arquivos

#Este módulo localiza e armazena o diretório do arquivo 'interface.glade'
from diretorio import diretorio

#Este módulo cria tabelas com os dados binários.
from tabelalista import tabelalista

#Este módulo exclui dados dos arquivos binários.
from excluir import excluir

#Este módulo serve para exibir caixas de diálogo com
#mensagens para o usuário
from dialogo import dialogo

#Este módulo altera dados nos arquivos binários
from confirmar_alteração import confirmar_alteração

#Este módulo grava dados nos arquivos binários
from gravar_registro import gravar_registro

import os
import getpass
import locale

idioma = locale.getdefaultlocale()
system_user = getpass.getuser() #obtém o nome do usuário do sistema linux

#Armazena o diretório dos arquivos binários nas variáveis
ac = '/home/' + system_user + '/snap/gerenciadorcs/current/bin/ac.bin'
asu = '/home/' + system_user + '/snap/gerenciadorcs/current/bin/asu.bin'
nu = '/home/' + system_user + '/snap/gerenciadorcs/current/bin/nu.bin'
se = '/home/' + system_user + '/snap/gerenciadorcs/current/bin/se.bin'
sx = '/home/' + system_user + '/snap/gerenciadorcs/current/bin/sx.bin'
ux = '/home/' + system_user + '/snap/gerenciadorcs/current/bin/ux.bin'

#Importa a biblioteca Gtk
import gi
gi.require_version('Gtk', "3.0")
from gi.repository import Gtk

#Aqui inicia o programa
class main_window:

    def __init__(self):

        #Indica que a interface, menus, janelas, módulos e caixas de diálogo
        #do programa serão carregadas a partir do conjunto de instruções contidos
        #no arquivo 'interface.glade'. Este arquivo foi criado no programa
        #Glade versão 3.22.1, o Glade é um construtor de interfaces de usuário
        #para GTK+ e GNOME.
        self.gladefile = diretorio()
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)

        #Constroi cada janela/tela e/ou módulo que compõe o programa,
        #estas definições estão contidas no arquivo 'interface.glade'
        self.main_window = self.builder.get_object('main_window')
        self.main_window.show()
        self.login = self.builder.get_object("login")
        self.new_user = self.builder.get_object("new_user")
        self.cadastrar = self.builder.get_object('window_cadastrar')
        self.exibir = self.builder.get_object('exibir')
        self.alterar = self.builder.get_object('window_alterar')
        self.lista = self.builder.get_object('lista')
        self.grid = self.builder.get_object('grid')
        self.dialogo_sobre = self.builder.get_object('dialogo_sobre')
        self.barra_menu = self.builder.get_object('barra_menu')
        self.dialogo = self.builder.get_object('dialogo')
        self.rotulo = self.builder.get_object('rotulo')

        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)

        #Esta variável serve para armazenar qual usuário está logado no programa,
        #controla quais informações ele irá armazenar e quais informações ele
        #pode acessar dentro do programa.
        self.aux = ""
      
        #Estas variáveis serão utilizadas no momento de exibir dados que
        #o usuário armazenou no banco de dados
        self.tabela_ux = ([])
        self.lista = ""

        #Estas variáveis armazenam itens/dados da lista gravados
        self.conta_ch = ""
        self.user_ch =  ""
        self.sx_ch = ""
        #Armazena temporáriamente os dados atuais para alteração
        self.conta_gravada = ""
        self.usuario_gravado = ""
        self.senha_gravada = ""

        #Armazena temporariamente os dados novos para gravação 
        self.conta_nova = ""
        self.usuario_novo = ""
        self.senha_nova = ""

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
                arq_ux = open(ux, 'r')
                arq_sx = open(sx, 'r')
                
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
                mlogin = ''
                if (cux == csx):
                    print("senha correta!")
                    if idioma == ('pt_BR', 'UTF-8'):
                        mlogin = "senha correta, login efetuado com sucesso!"

                    elif idioma == ('en_US', 'UTF-8'):
                        mlogin = "correct password, login successfully!"
                        
                    else:
                        mlogin = "correct password, login successfully!"
    
                    self.dialogo_c(self.dialogo, self.rotulo, mlogin)
                    self.login.hide()
                    self.aux = aux #armazena o nome do usuário logado em 'self.aux'
                    self.chave = 0
                else:
                    print("senha incorreta!")
                    if idioma == ('pt_BR', 'UTF-8'):
                        mlogin = "Usuário e/ou senha incorretas!"

                    elif idioma == ('en_US', 'UTF-8'):
                        mlogin = "Username and / or password incorrect!"
                        
                    else:
                        mlogin = "Username and / or password incorrect!"

                    self.dialogo_c(self.dialogo, self.rotulo, mlogin)                    

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
                self.chave_nuser = 1

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
                        mnuser = ''
                        if (nuser == "" or userp == ""):

                            if idioma == ('pt_BR', 'UTF-8'):
                                mnuser = 'Você não pode deixar campos em branco!'

                            elif idioma == ('en_US', 'UTF-8'):
                                mnuser = 'You cannot leave fields blank!'
                            else:
                                mnuser = 'you cannot leave fields blank!'
                            self.dialogo_c(self.dialogo, self.rotulo, mnuser)
                            ad = nuser
                        else:
                            user_check = open(ux, 'r')
                            for linha in user_check:
                                linha = linha.rstrip()
                                #a variável ad armazena cada linha do arquivo uma por vez
                                ad = linha
                                #Se o valor contido em alguma linha corresponder ao
                                #ao nome do usuário o valor de 'self.chave_check' será 1
                                if (ad == nuser):
                                    print(ad, nuser)
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
                        if idioma == ('pt_BR', 'UTF-8'):
                            mnuser = "Nome de usuário já cadastrado, tente outro nome!"

                        elif idioma == ('en_US', 'UTF-8'):
                            mnuser = "Username already registered, try another name!"
                        else:
                            mnuser = "Username already registered, try another name!"
                        
                        self.dialogo_c(self.dialogo, self.rotulo, mnuser)
                        self.user_name.set_text("")
                        self.user_p.set_text("")
                        ad = ""
                        nuser = ""
                        self.chave_check = 2
                        self.chave_nuser = 1
                        
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
                        arq_ux = open(ux, 'a+')
                        arq_sx = open(sx, 'a+')
                        arq_ux.write("{}\n".format(nuser))
                        arq_sx.write("{}\n".format(userp))
                        arq_ux.seek(0)
                        arq_sx.seek(0)
                        arq_ux.close()
                        arq_sx.close()

                        if idioma == ('pt_BR', 'UTF-8'):
                            mnuser = "usuário cadastrado com sucesso, faça login para acessar o programa!"

                        elif idioma == ('en_US', 'UTF-8'):
                            mnuser = "user registered successfully, login to access the program!"
                        else:
                            mnuser = "user registered successfully, login to access the program!"
                        
                        self.dialogo_c(self.dialogo, self.rotulo, mnuser)
                        self.user_name.set_text("")
                        self.user_p.set_text("")
                        self.new_user.hide()
                        self.chave_nuser = 0
                        
                
        #Se usuário e senha estiverem corretos ele exibe o 'menu' do sistema.
        if (cux == csx):

            self.exibir.show()

            #O módulo "tabelalista" cria uma tabela com os dados cadastrados
            #do usuário
            self.tabela_ux = tabelalista(self.aux, ac, nu, se, asu)

            self.lista = Gtk.ListStore(str, str, str)
            for software_ref in self.tabela_ux:
                self.lista.append(list(software_ref))

            self.current_filter_language = None

            self.language_filter = self.lista.filter_new()

            cabecalho = []
            if idioma == ('pt_BR', 'UTF-8'):
                cabecalho = ["Conta", "Usuário", "Senha"]
            elif idioma == ('en_US', 'UTF-8'):
                cabecalho = ["Account", "User", "Password"]
            else:
                cabecalho = ["Account", "User", "Password"]

            treeview = Gtk.TreeView.new_with_model(self.language_filter)
            for i, column_title in enumerate([cabecalho[0], cabecalho[1], cabecalho[2]]):
                renderer = Gtk.CellRendererText()
                column = Gtk.TreeViewColumn(column_title, renderer, text=i)
                treeview.append_column(column)

            scrollable_treelist = Gtk.ScrolledWindow()
            scrollable_treelist.set_vexpand(True)
            self.grid.attach(scrollable_treelist, 0, 0, 8, 10)

            scrollable_treelist.add(treeview)

            self.grid.show_all()

            #Conecta sinais para que a lista recebe clique e duplo clique
            treeview.connect('row-activated', self.on_lista_row_activated)
            treeview.connect('cursor-changed', self.on_cursor_changed)
            self.treeview_selection = treeview.get_selection()
                
    #Ativa o clique duplo na lista
    def on_lista_row_activated(self, widget, path, column):
        print("clique duplo")
        model, iter = self.treeview_selection.get_selected()
        print('path= %s, column= %s' % (path, column))
        print('Model = %s ,Iter =  %s' % (model,iter))
        print(" COLUNA =0 - DADO =  %s  " % ( model.get_value(iter,0)))
        print(" COLUNA =1 - DADO =  %s  " % ( model.get_value(iter,1)))
        print(" COLUNA =2 - DADO =  %s  " % ( model.get_value(iter,2)))

    #Ativa o clique único na lista
    def on_cursor_changed(self, widget):
        print ("clique único")
        model,iter = self.treeview_selection.get_selected()
        print ('Model = %s ,Iter =  %s' % (model,iter))
        print ("COLUNA =0 - DADO =  %s  " % ( model.get_value(iter,0)))
        print ("COLUNA =1 - DADO =  %s  " % ( model.get_value(iter,1)))
        print ("COLUNA =2 - DADO =  %s  " % ( model.get_value(iter, 2)))
        self.conta_ch = model.get_value(iter, 0)
        self.user_ch =  model.get_value(iter, 1)
        self.sx_ch =    model.get_value(iter, 2)
        print ("o valor armazenado em conta_ch é: ", self.conta_ch)
        print ("o valor armazenado em user_ch é: ", self.user_ch)
        print ("o valor armazenado em sx_ch é: ", self.sx_ch)

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

    def on_menu_ajuda_sobre_activate(self, object, data=None):
        self.dialogo_sobre.show()
        response = self.dialogo_sobre.run()
        if (response == Gtk.ResponseType.OK):
            self.dialogo_sobre.hide()
        if (response == Gtk.ResponseType.DELETE_EVENT):
            self.dialogo_sobre.hide()

    def on_menu_sair_activate(self, object, data=None):
        print("quit with menu-arquivo-sair")
        self.main_window.close()
        Gtk.main_quit()

    #Se o botão 'Fechar' receber um clique limpa a tabela e a lista
    #e fecha todo o programa
    def on_fechar_clicked(self, object, data=None):
        self.tabela_ux = ([])
        self.lista.clear()
        print("Close from 'exibir' on 'Fechar' button")
        self.main_window.close()
        Gtk.main_quit()

    def on_excluir_item_clicked(self, object, data=None):

        if (self.conta_ch == "" and self.user_ch == "" and self.sx_ch == ""):
            msg_nexcluir = ''
            if idioma == ('pt_BR', 'UTF-8'):
                msg_nexcluir = "Nenhum item foi selecionado para exclusão!"

            elif idioma == ('en_US', 'UTF-8'):
                msg_nexcluir = "No items were selected for deletion!"
            else:
                msg_nexcluir = "No items were selected for deletion!"
            self.dialogo_c(self.dialogo, self.rotulo, msg_nexcluir)
            self.conta_ch = ""
            self.user_ch = ""
            self.sx_ch = ""
        else:
            #O módulo 'excluir' exclui um ítem da lista e atualiza os arquivos binários
            msg_excluir = excluir(self.aux, ac, nu, se, asu, self.conta_ch, self.user_ch, self.sx_ch)
            self.dialogo_c(self.dialogo, self.rotulo, msg_excluir)

            #Atualiza a lista a ser exibida
            self.exibir.hide()
            self.tabela_ux = ([])
            self.lista.clear()
            self.tabela_ux = tabelalista(self.aux, ac, nu, se, asu)
            for software_ref in self.tabela_ux:
                self.lista.append(list(software_ref))
            self.exibir.show()
            self.conta_ch = ""
            self.user_ch = ""
            self.sx_ch = ""
        
        
    #Com o usuário logado e o 'menu' visível se o usuário clicar no botão
    #'cadastar' ele esconde o 'menu' e abre o módulo 'Cadastrar uma nova senha'
    def on_botao_cadastrar_clicked(self, object, data=None):
        #Constrói e ativa os campos para inserir os dados à serem alterados
        self.conta_name = self.builder.get_object('conta_name')
        self.nome_usuario = self.builder.get_object('nome_usuario')
        self.conta_ps = self.builder.get_object('conta_ps')
        
        response = self.cadastrar.run()
        self.cadastrar.hide()
        self.conta_name = self.conta_name.set_text("")
        self.nome_usuario = self.nome_usuario.set_text("")
        self.conta_ps = self.conta_ps.set_text("")
        
    #Esta função grava a conta e a senha que o usuário deseja armazenar
    def on_botao_gravar_registro_clicked(self, object, data=None):

        #Armazena os dados inseridos em variáveis temporárias
        conta_name = self.conta_name.get_text()
        nome_usuario = self.nome_usuario.get_text()
        conta_ps = self.conta_ps.get_text()

        if (conta_name == "" or nome_usuario == "" or conta_ps == ""):
            msg_cb = ""
            if idioma == ('pt_BR', 'UTF-8'):
                msg_cb = "Nenhum campo pode estar em branco!"
                
            elif idioma == ('en_US', 'UTF-8'):
                msg_cb = "No field can be empty!"

            else:
                msg_cb = "No field can be empty!"

                
            self.dialogo_c(self.dialogo, self.rotulo, msg_cb)
            self.conta_name.set_text("")
            self.nome_usuario.set_text("")
            self.conta_ps.set_text("")
        else:
            #O módulo 'gravar_registro' recebe os dados digitados na caixa de diálogo
            #'window_cadastrar' e grava nos arquivos binários
            msg_gravar = gravar_registro(self.aux, conta_name, nome_usuario, conta_ps, ac, nu, se, asu, self.tabela_ux)
            self.dialogo_c(self.dialogo, self.rotulo, msg_gravar)

            if (msg_gravar == "Dados Gravados com Sucesso" or msg_gravar == "Data Saved Successfully"):
                #Fecha a caixa de dialogo 'window_cadastrar' e apaga os campos digitados
                self.cadastrar.hide()
                self.conta_name.set_text("")
                self.nome_usuario.set_text("")
                self.conta_ps.set_text("")

                #Atualiza a lista com as informações adicionadas
                self.tabela_ux = ([])
                self.lista.clear()
                self.tabela_ux = tabelalista(self.aux, ac, nu, se, asu)
                for software_ref in self.tabela_ux:
                    self.lista.append(list(software_ref))

    #Fecha o dialogo 'window_cadastrar' e volta para a lista
    def on_botao_voltarc_clicked(self, objetc, data=None):
        self.cadastrar.hide()
        self.conta_name = self.conta_name.set_text("")
        self.nome_usuario = self.nome_usuario.set_text("")
        self.conta_ps = self.conta_ps.set_text("")


        
    #Abre a caixa de diálogo 'window_alterar' se o botão 'alterar' receber um clique
    def on_botao_alterar_clicked(self, object, data=None):
        
        #Constrói e ativa os campos para inserir os dados à serem alterados
        self.conta_nova = self.builder.get_object('conta_nova')
        self.usuario_novo = self.builder.get_object('usuario_novo')
        self.senha_nova = self.builder.get_object('senha_nova')

        #Grava nessas variáveis os dados que serão alterados
        self.conta_gravada = self.conta_ch
        self.usuario_gravado = self.user_ch
        self.senha_gravada = self.sx_ch

        #Verifica se um item da lista foi selecionado, se não exibe um diálogo
        #ao usuário pra selecionar um item na lista para alterar, se sim abre
        #a caixa de diálogo 'window_alterar'
        if (self.conta_ch == "" and self.user_ch == "" and self.sx_ch == ""):
            msg_selecione_item = ""
            if idioma == ('pt_BR', 'UTF-8'):
                msg_selecione_item = "Selecione um item da lista para alterar"
            elif idioma == ('en_US', 'UTF-8'):
                msg_selecione_item = "Select an item from the list to change"
            else:
                msg_selecione_item = "Select an item from the list to change"
                
            self.dialogo_c(self.dialogo, self.rotulo, msg_selecione_item)
        else:
            response = self.alterar.run()
            print(response)
            self.alterar.hide()

    #Se o usuário clicar no botão 'x' no canto direito da caixa de diálogo
    #'window_alterar' irá fechar a caixa de diálogo e apagar qualquer coisa
    #digitada nos campos disponíveis
    def on_window_alterar_delete_event(self, objtect, data=None):
        self.conta_nova.set_text("")
        self.usuario_novo.set_text("")
        self.senha_nova.set_text("")  

    #Verifica os campos digitados e faz as alterações nos dados cadastrados
    def on_botao_confirmar_alteracao_clicked(self, object, data=None):
        
        #Armazena os dados atuais em variáveis temporárias
        conta_gravada = self.conta_gravada
        usuario_gravado = self.usuario_gravado
        senha_gravada = self.senha_gravada

        #Armazena os dados novos em variáveis temporárias
        conta_nova = self.conta_nova.get_text()
        usuario_novo = self.usuario_novo.get_text()
        senha_nova = self.senha_nova.get_text()

        #Não é obrigatório o preenchimento da "conta" e do "usuário"
        #a menos que o usuário queira alterar essas informações
        #A senha atual ou a nova senha da conta é obrigatória para fazer as alterações
        #Verifica se os campos preenchidos atendem aos critérios para alteração
        if (conta_nova == ""):
            conta_nova = conta_gravada
        if (usuario_novo == ""):
            usuario_novo = usuario_gravado
        if (senha_nova == ""): #Não é permitido deixar o campo de senha em branco
            msg_senha_vazia = ''
            if idioma == ('pt_BR', 'UTF-8'):
                msg_senha_vazia = 'Você não pode cadastrar uma senha em branco'
            elif idioma == ('en_US', 'UTF-8'):
                msg_senha_vazia = 'You cannot register a blank password'
            else:
                msg_senha_vazia = 'You cannot register a blank password'
            self.dialogo_c(self.dialogo, self.rotulo, msg_senha_vazia)
            self.conta_nova = self.conta_nova.set_text("")
            self.usuario_novo = self.usuario_novo.set_text("")
            self.senha_nova = self.senha_nova.set_text("")
        else:
            #chama o módulo "confirmar_alteração" para verificar os dados e
            #fazer a alteração nos arquivos binários
            msg_alterar_s = confirmar_alteração(
                self.aux, ac, nu, se, asu, 
                conta_gravada, usuario_gravado, 
                senha_gravada, conta_nova, usuario_novo,
                senha_nova
                )
            self.dialogo_c(self.dialogo, self.rotulo, msg_alterar_s)

            #Fecha a caixa de diálogo "window_alterar" e limpa os campos digitados
            self.alterar.hide()
            self.conta_nova = self.conta_nova.set_text("")
            self.usuario_novo = self.usuario_novo.set_text("")
            self.senha_nova = self.senha_nova.set_text("")

            #recria a lista com os dados atualizados para exibição
            self.tabela_ux = ([])
            self.lista.clear()
            self.tabela_ux = tabelalista(self.aux, ac, nu, se, asu)
            for software_ref in self.tabela_ux:
                self.lista.append(list(software_ref))

    #Fecha a caixa de diálogo "window_alterar" volta para a lista
    #Limpa quaisquer campos digitados pelo usuário
    def on_botao_voltara_clicked(self, object, data=None):
        self.alterar.hide()
        self.conta_nova.set_text("")
        self.usuario_novo.set_text("")
        self.senha_nova.set_text("")
        

        
if __name__ == "__main__":
    main = main_window()
    Gtk.main()
