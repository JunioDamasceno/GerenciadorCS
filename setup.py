from setuptools import setup

setup( name = 'gerenciadorcs',
       version = '3.1',
       author = 'Junio da Silva Damasceno',
       author_email = 'juniowin@yahoo.com.br',
       packages = ['gerenciadorcs'],
       data_files=[('glade',
                    ['gerenciadorcs/interface-en-US.glade',
                     'gerenciadorcs/interface-pt-BR.glade'])],
       description = 'um gerenciador de contas, usuários e senhas',
       url = 'https://github.com/JunioDamasceno/gerenciadorcs',
       license = 'MIT',
       keywords = ['gerenciador de senhas', 'Key manager', 'keymanager'],
       classifiers = [
           'Development Status :: 5 - Production/Stable',
           'Intended Audience :: Developers',
           'Licence :: OSI Aproved :: MIT licence',
           'Natural Language :: Portuguese (Brazilian)',
       ]
)

