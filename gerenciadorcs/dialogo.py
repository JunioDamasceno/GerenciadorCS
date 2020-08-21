#Este módulo é usado para exibir caixas de diálogo dentro do programa
#principal. Ele retorna mensagens para o usuário

#É necessário importar a biblioteca Gtk para o módulo dialogo funcionar
import gi
gi.require_version('Gtk', "3.0")
from gi.repository import Gtk

#Esta é a função 'dialogo'
def dialogo(dialogo, rotulo, mensagem):
            
            dialogo.show()
            rotulo.set_label(mensagem)
            response = dialogo.run()
            if response == Gtk.ResponseType.OK:
                dialogo.hide()
            if response == Gtk.ResponseType.DELETE_EVENT:
                dialogo.close()
            return response
