from setuptools import setup

setup( name = 'gerenciadorcs',
       version = '1.0.0',
       author = 'Junio da Silva Damasceno',
       author_email = 'juniowin@yahoo.com.br',
       packages = ['gerenciadorcs'],
       data_files=[
           ('bin', [
               'gerenciadorcs/ac.bin',
               'gerenciadorcs/asu.bin',
               'gerenciadorcs/nu.bin',
               'gerenciadorcs/se.bin',
               'gerenciadorcs/sx.bin',
               'gerenciadorcs/ux.bin'
               ]
            ),
           ('png', [
               'gerenciadorcs/icone_64x64.png',
               'gerenciadorcs/icone_128x128.png'
               ]
            ),
           ('svg', [
               'gerenciadorcs/icone_64x64.svg',
               'gerenciadorcs/icone_128x218.svg'
               ]
            ),
           ('ico', [
                'gerenciadorcs/icone_64x64.ico',
                'gerenciadorcs/icone_128x128.ico'
               ]
            ),
           ('desktop', ['gerenciadorcs/gerenciadorcs.desktop']),
           ('glade', ['gerenciadorcs/interface.glade']),
           ],
       description = 'um gerenciador de contas e senhas de usuarios',
       url = 'https://github.com/JunioDamasceno/gerenciadorcs',
       license = 'MIT',
       keywords = 'gerenciador de senhas',
       classifiers = [
           'Development Status :: 5 - Production/Stable',
           'Intended Audience :: Developers',
           'Licence :: OSI Aproved :: MIT licence',
           'Natural Language :: Portuguese (Brazilian)',
       ]
)

