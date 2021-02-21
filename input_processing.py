from utils import commands_list, commands_dict, admin_commands


class Input:
    def __init__(self):
        pass

    def process(self, command, caller):
        args = command.split()  # [ 'comando', 'arg1', 'arg2', ... ]
        name = args[0]  # Nome do comando

        if not(name in commands_list):
            # TODO
            # Melhorar esse print
            print('''Falha. Comando inexistente.
            
Lista de comandos:''')
            
            for i in commands_list:
                print(i)

            return 1
        
        if not(len(args) >= commands_list[name][0] and len(args) <= commands_list[name][1] ):
            print("Falha. Quantidade de argumentos inválida")
            
            commands_dict[command].help()

            return 1

        if not(caller.permission == 'admin' and command in admin_commands):
            print('''Acesso negado. Você não possui permissão para isto.
            
Lista de comandos restritos:''')

            for i in admin_commands:
                print(i)
            
            return 1

        return self.call_command(args[0], args[1:], caller.permission)
    
    def call_command(self, command, args, permissions):
        print(command)
        print(args)
        
        return commands_dict[command](*args)

