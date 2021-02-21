from utils import commands_list, commands_dict, admin_commands


class Input:
    def __init__(self):
        pass

    def process(self, command, caller, filesystem):
        args = command.split()  # [ 'comando', 'arg1', 'arg2', ... ]
        name = args[0]  # Nome do comando

        if not(name in commands_list):
            print("Falha. Comando inexistente.\n\nLista de comandos:")
            
            for i in commands_list:
                print(i)

            return 1
        
        if not(len(args) >= commands_list[name][0] and len(args) <= commands_list[name][1] ):
            print("Falha. Quantidade de argumentos inválida")
            
            commands_dict[command].help()

            return 1

        if not(caller.permission == 'admin' and command in admin_commands):
            print("Acesso negado. Você não possui permissão para isto.\n\nLista de comandos restritos:")

            for i in admin_commands:
                print(i)
            
            return 1

        # Concatenei filesystem com os args, desta forma o filesystem sempre vai ser
        # o primeiro argumento passado...

        # TODO
        # Será que devo passar o filesystem apenas para classes específicas ?
        self.call_command(args[0], [filesystem] + args[1:])
        return 0
    
    def call_command(self, command, args):
        print(command)
        print(args)
        
        # TODO
        # Passar filesystem
        return commands_dict[command](*args)

