from input_processing import Input
from entities import User, Filesystem

from user_management import User_utils, user_db

user_db['admin'] = User('admin', '123', 'admin')

def login():
    print("Faça o seu login:\n\n")
    while (1):    
        username = str(input("Nome de usuário: "))
        passwd = str(input("Senha"))
        current_user = User_utils.login_user(username, passwd)
        if not(current_user):
            break
        
        print("Usuário ou senha inválidos, tente novamente")

login()

# Instanciando o sistema de arquivos
fs = Filesystem()
    
while (1):
    command = str(input(f"{'/'.join(fs.get_path())}$ "))
    inp = Input()
    # Checar valor de retorno para possíveis erros
    inp.process(command, current_user, fs)
    print(f'path: {fs.path}')
    print(f'filesystem: {fs.fs}')
    