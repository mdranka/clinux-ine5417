# File and Directory management classes

class Files():
    def __init__(self, filesystem, filename):
        self.filesystem = filesystem
        self.filename = filename

    
    def get_dir_dict(self):
        # d recebe root
        d = self.filesystem.fs['']  
        # Vamos percorrer até chegarmos no diretório atual
        for dir in self.filesystem.current_dir:
            d = d[dir]
        
        return d

class Mkdir(Files):
    def __init__(self, filesystem, dir_name):
        Files.__init__(self, filesystem, dir_name)
        self.create_dir()
    
    def create_dir(self):
        self.get_dir_dict()[self.filename] = {}


class Touch(Files):
    def __init__(self, filesystem, filename):
        Files.__init__(self, filesystem, filename)
        self.create_file()
    
    def create_file(self):
        self.get_dir_dict()[self.filename] = []

class Rm(Files):
    def __init__(self, filename, filesystem, recursive):
        Files.__init__(self, filename, filesystem)
        # TODO
        # Implement recursive mode
        self.recursive = recursive
        self.remove_file()

    def remove_file(self):
        #TODO
        pass

class Ls(Files):
    def __init__(self, filesystem):
        self.list_dir(filesystem)

    def list_dir(self, filesystem):
        for i in self.get_dir_dict():
            print(i)

