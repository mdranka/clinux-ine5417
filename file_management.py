# File and Directory management classes

class Files():
        
    # Método privado
    @staticmethod
    def __get_dir_dict(filesystem):
        # d recebe root
        d = filesystem.fs
        # Vamos percorrer até chegarmos no diretório atual
        for dir in filesystem.current_dir:
            d = d[dir]
        
        print(f'd: {d}')
        return d
    
    @staticmethod
    def mkdir(filesystem, filename):
        Files.__get_dir_dict(filesystem)[filename] = {}
        
    @staticmethod
    def touch(filesystem, filename):
        Files.__get_dir_dict(filesystem)[filename] = []

    @staticmethod
    def rm(filesystem, filename, recursive):
        #TODO
        pass

    @staticmethod
    def ls(filesystem):
        print(f"filesystem ls: {filesystem.fs}")
        for i in Files.__get_dir_dict(filesystem):
            print(i)

    