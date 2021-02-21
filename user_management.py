from db import user_db
from user import User

# Admin methods

class Useradd:
    def __init__(self, username):
        self.username = username
        self.create_user(username)
    
    def create_user(self, username):
        passwd = str(input("Escreva sua senha: \n"))
        user_db[username] = User(username, passwd)

    def delete_user(self, username):
        user_db.pop(username)
        print(f"Deleted user {username}")

    def list_users(self):
        for i in user_db:
            print(i)

    @staticmethod
    def help():
        print('''Uso:
useradd username [permissao]
        
Onde permissão poder ser "common" ou "admin"''')


        


    