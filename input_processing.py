from command_caller import Command_caller


class Input:
    def __init__(self, caller):
        self.caller = caller

    def process(self, command):
        args = command.split()  # [ 'comando', 'arg1', 'arg2', ... ]
        name = args[0]  # Nome do comando
        commands = self.caller.commands
        current_user = self.caller.user

        if not(name in commands):
            print("Falha. Comando inexistente.\n\nLista de comandos:")
            
            for i in commands:
                print(i)

            return 1
        
        if not(len(args) >= commands[name][1][0] and len(args) <= commands[name][1][1] ):
            print("Falha. Quantidade de argumentos inválida")
            
            # TODO
            # Fix this
            commands[name].help()

            return 1
        
        if (current_user.permission == 'common' and name in self.caller.admin_commands):
            print("Acesso negado. Você não possui permissão para isto.\n\nLista de comandos restritos:")

            for i in self.caller.admin_commands:
                print(i)
            
            return 1
       
        self.caller.call(name, args[1:])
        
        return 0

