from user_management import Useradd
from file_management import Files

# Nome do comando : [ mínimo de argumentos, máximo de argumentos ]
# é 'list' mas é dicionário! Talvez um nome melhor ? ...

commands_dict = { 'useradd': [Useradd, [2,3]], 'mkdir': [Files.mkdir, [2,2]], 'touch': [Files.touch, [2,2]], 'rm': [Files.rm, [2,3]], 
                  'ls': [Files.ls, [1,1]] }

admin_commands = { 'useradd' }
