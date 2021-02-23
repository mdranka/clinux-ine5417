from user_management import User_utils
from file_management import File_utils

# Nome do comando : [ mínimo de argumentos, máximo de argumentos ]
# é 'list' mas é dicionário! Talvez um nome melhor ? ...

commands_dict = { 'useradd': [User_utils.useradd, [2,3]], 'mkdir': [File_utils.mkdir, [2,2]], 'touch': [File_utils.touch, [2,2]], 'rm': [File_utils.rm, [2,3]], 
                  'ls': [File_utils.ls, [1,1]], 'cd': [File_utils.cd, [2,2]] }

admin_commands = { 'useradd' }
