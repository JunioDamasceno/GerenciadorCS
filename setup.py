from setuptools import setup

setup( name = 'gerenciadorcs',
       version = '3.0',
       author = 'Junio da Silva Damasceno',
       author_email = 'juniowin@yahoo.com.br',
       packages = ['gerenciadorcs'],
       data_files=[
           ('png', ['gerenciadorcs/icone_64x64.png']),
           ('desktop', ['gerenciadorcs/gerenciadorcs.desktop']),
           ('glade', ['gerenciadorcs/interface.glade']),
           ],
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

