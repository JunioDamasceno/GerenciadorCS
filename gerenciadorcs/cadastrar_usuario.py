#Este modulo cria novos usuários

def cadastrar_usuario(nomeu, senhau, idioma, ux, sx):

    #codigo
    if (nomeu == "" or senhau == ""):
        if idioma == ('pt_BR', 'UTF-8'):
            return('Você não pode deixar campos em branco!', 0)
        elif idioma == ('en_US', 'UTF-8'):
            return('You cannot leave fields blank!', 0)
        elif idioma ==('es_ES', 'UTF-8'):
            return("No puedes dejar los campos en blanco!", 0)
        else:
            return('you cannot leave fields blank!', 0)
    else:
        nome_usuario = nomeu.encode('utf-8').hex()
        senha_usuario = senhau.encode('utf-8').hex()

        checar_usuario = open(ux, 'r')
        usuario_existente = 0
        for linha in checar_usuario:
            linha = linha.rstrip()
            if (linha == nome_usuario):
                usuario_existente = 1
                if idioma == ('pt_BR', 'UTF-8'):
                    return("Nome de usuário já cadastrado, tente outro nome!", 1)
                elif idioma == ('en_US', 'UTF-8'):
                    return("Username already registered, try another name!", 1)
                elif idioma == ('es_ES', 'UTF-8'):
                    return("Nombre de usuario ya registrado, pruebe con otro nombre!", 1)
                else:
                    return("Username already registered, try another name!", 1)

        checar_usuario.seek(0)
        checar_usuario.close()

        if(usuario_existente == 0):
            checar_usuario = open(ux, 'a+')
            checar_senha = open(sx, 'a+')
            checar_usuario.write("{}\n".format(nome_usuario))
            checar_senha.write("{}\n".format(senha_usuario))
            checar_usuario.seek(0)
            checar_senha.seek(0)
            checar_usuario.close()
            checar_senha.close()
            if idioma == ('pt_BR', 'UTF-8'):
                return("usuário cadastrado com sucesso, faça login para acessar o programa!", 2)
            elif idioma == ('en_US', 'UTF-8'):
                return("user registered successfully, login to access the program!", 2)
            elif idioma == ('es_ES', 'UTF-8'):
                return("usuario registrado con éxito, inicie sesión para acceder al programa!", 2)
            else:
                return("user registered successfully, login to access the program!", 2)
