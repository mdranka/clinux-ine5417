from input_processing import Input
from entities import User, Filesystem

current_user = User('teste', 'teste')
fs = Filesystem()
    
while (1):
    command = str(input(">> "))
    inp = Input()
    # Checar valor de retorno para possíveis erros
    inp.process(command, current_user, fs)
    print(f'current_dir: {fs.current_dir}')
    print(f'filesystem: {fs.fs}')
    