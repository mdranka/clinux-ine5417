from db import user_db
from sys import exit
from entities import User

class User_utils:
    
    @staticmethod
    def useradd(username, caller):
        if (caller.permission == 'common'):
            print("Falha. Você não tem permissão para isto")
        else:
            passwd = str(input("Escreva sua senha: \n"))
            user_db[username] = User(username, passwd, 'common')

    @staticmethod
    def rmuser(username, caller):
        if (caller.permission == "common"):
            print("Falha. Você não tem permissão para isto")
            
            # if (username != caller.username):
            #     print("Falha. Você não tem permissão para isto")
            # else:
            #     user_db.pop(username)
            #     print("Seu usuário foi apagado.\nSaindo do sistema...")
            #     # Chamando sys.exit
            #     exit()
        
        else:  # Sou admin
            user_db.pop(username)
            print(f"Deleted user {username}")

    @staticmethod
    def lsusers():
        for i in user_db:
            print(i)

    @staticmethod
    def login_user(username, passwd):
        if (username in user_db):
            if (user_db[username].password == passwd):
                return user_db[username]
            return 1
        return 1

    # TODO:
    # Implementar help para os outros comandos de User_utils
    @staticmethod
    def help():
        print("Uso:\nuseradd username [permissao]\n\nOnde permissão poder ser 'common' ou 'admin'")


        


    