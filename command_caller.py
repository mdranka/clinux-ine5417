from user_management import *
from file_management import *

class Command_caller:
    def __init__(self, user, filesystem):
        self.commands = { 'useradd': [User_utils.useradd, [2,3]], 'mkdir': [File_utils.mkdir, [2,2]], 'touch': [File_utils.touch, [2,2]], 'rm': [File_utils.rm, [2,3]], 
                     'ls': [File_utils.ls, [1,1]], 'cd': [File_utils.cd, [2,2]] }
        
        self.user_management_commands = {'useradd'}

        self.admin_commands = {'useradd'}

        self.user = user
        self.filesystem = filesystem

    def call(self, command_name, args):
        # args é uma lista de argumentos
        
        # Se for um comando de gerência de usuário, é desnecessário eu passar o objeto
        # de Filesystem
        if command_name in self.user_management_commands:
            args = [self.user] + args
        
        # Concatenei user e filesystem com os args, desta forma o user e o filesystem sempre vão ser
        # os primeiros argumentos passados...
        else: 
            args = [self.user, self.filesystem] + args
        
        self.commands[command_name][0](*args)



