class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Por padrão, todo usuário é criado como 'comum'
        self.permission = 'common'

class Filesystem:
    def __init__(self):
        self.current_dir = []
        self.fs = {}
        