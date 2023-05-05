class Connect4Action:
    
    __colFrom: int
    __rowFrom: int
    __colTo: int
    __rowTo: int

    def __init__(self, colFrom: int, rowFrom: int, colTo: int, rowTo: int):
        self.__colFrom = colFrom
        self.__rowFrom = rowFrom
        self.__colTo = colTo
        self.__rowTo = rowTo
        

    def get_colFrom(self):
        return self.__colFrom

    def get_rowFrom(self):
        return self.__rowFrom

    def get_colTo(self):
        return self.__colTo

    def get_rowTo(self):
        return self.__rowTo
        
