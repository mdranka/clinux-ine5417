class User:
    def __init__(self, username, password, permission):
        self.username = username
        self.password = password
        # Por padrão, todo usuário é criado como 'comum'
        self.permission = permission

class Filesystem:
    def __init__(self):
        self.path = ['/']
        # Empty string is root
        self.fs = {'/': {}}
    
    def get_path(self):
        return self.path
    
    def pop_path(self):
        self.path.pop()
    
    def append_path(self, file):
        self.path.append(file)