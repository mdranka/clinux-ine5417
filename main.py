from input_processing import Input
from entities import User, Filesystem

while (1):
    current_user = User('teste', 'teste')
    fs = Filesystem()
    command = str(input(">> "))
    inp = Input()
    # Checar valor de retorno para possíveis erros
    inp.process(command, current_user, fs)
    