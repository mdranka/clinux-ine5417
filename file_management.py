# File and Directory management classes

class File_utils():
        
    # Método privado
    @staticmethod
    def get_current_dir(filesystem):
        # d recebe root
        d = filesystem.fs
        # Vamos percorrer até chegarmos no diretório atual
        for dir in filesystem.get_path():
            d = d[dir]
        
        return d
    
    @staticmethod
    def mkdir(filesystem, filename):
        File_utils.get_current_dir(filesystem)[filename] = {}
        
    @staticmethod
    def touch(filesystem, filename):
        File_utils.get_current_dir(filesystem)[filename] = []

    @staticmethod
    def rm(filesystem, filename, recursive):
        #TODO
        pass

    @staticmethod
    def ls(filesystem):
        for i in File_utils.get_current_dir(filesystem):
            print(i)

    @staticmethod
    def cd(filesystem, path):
        
        d = File_utils.get_current_dir(filesystem)

        if (path == ".."):
            if (len(filesystem.get_path()) == 1):
                print("Falha. Você está na pasta raíz")
            else:
                filesystem.pop_path()
        
        elif (path not in File_utils.get_current_dir(filesystem)):
            print(f"Falha. Diretório {path} não encontrado")

        elif (isinstance(d[path], list)):
            print(f"Falha. {path} não é um diretório")

        else:
            filesystem.append_path(path)
        


        


    