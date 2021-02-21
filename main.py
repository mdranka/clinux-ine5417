from input_processing import Input
from user import User

while (1):
    current_user = User('teste', 'teste')
    command = str(input(">> "))
    inp = Input()
    # Checar valor de retorno para possíveis erros
    inp.process(command, current_user)
    