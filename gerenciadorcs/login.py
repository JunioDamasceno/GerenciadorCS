# Este módulo gerencia logins de usuaŕios

def login(nomeu, senhau, idioma, ux, sx):
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
        checar_senha = open(sx, 'r')
        usuario_existente = [0, 0]

        for linha in checar_usuario:
            linha = linha.rstrip()
            if (linha == nome_usuario):
                usuario_existente[0] = 1
        checar_usuario.seek(0)
        checar_usuario.close()

        for linha in checar_senha:
            linha = linha.rstrip()
            if (linha == senha_usuario):
                usuario_existente[1] = 1
        checar_senha.seek(0)
        checar_senha.close()

        if (usuario_existente[0] == 1 and usuario_existente[1] == 1):
            if idioma == ('pt_BR', 'UTF-8'):
                return ("senha correta, login efetuado com sucesso!", 2)
            elif idioma == ('en_US', 'UTF-8'):
                return ("correct password, login successfully!", 2)
            elif idioma == ('es_ES', 'UTF-8'):
                return ("contraseña correcta, inicio de sesión realizado con éxito!", 2)
            else:
                return ("correct password, login successfully!", 2)
        else:
            if idioma == ('pt_BR', 'UTF-8'):
                return ("Usuário e/ou senha incorretas!", 1)
            elif idioma == ('en_US', 'UTF-8'):
                return ("Username and / or password incorrect!", 1)
            elif idioma == ('es_ES', 'UTF-8'):
                return ("Usuario y/o contraseña incorrectos!", 1)

            else:
                return ("Username and / or password incorrect!", 1)


