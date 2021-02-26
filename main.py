from input_processing import Input, Command_caller
from user_management import User_utils
from entities import User, Filesystem
from colorama import Fore, Back, Style
from db import user_db

user_db['admin'] = User('admin', '123', 'admin')


current_user = User_utils.login()
# Instanciando o sistema de arquivos
fs = Filesystem()

caller = Command_caller(current_user, fs)
inp = Input(caller)
    
while (1):
    command = str(input(f"{Fore.GREEN}{current_user.username}:{Fore.BLUE}{'/'.join(fs.get_path())}{Style.RESET_ALL}$ "))
    
    inp.process(command)

    # Para debug:
    # print(f'path: {fs.path}')
    # print(f'filesystem: {fs.fs}')
    