from user_management import Useradd

# Nome do comando : [ mínimo de argumentos, máximo de argumentos ]
# é 'list' mas é dicionário! Talvez um nome melhor ? ...
commands_list = { 'useradd': [2, 3] }

commands_dict = { 'useradd': Useradd }

admin_commands = { 'useradd' }


# file_system = { '/' : { 'home' : {'jpadn', 'teste'}} }
file_system = {}