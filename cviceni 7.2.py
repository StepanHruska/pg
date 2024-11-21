class ImutableInteger:
    def __init__(self, number):
        self.__number = number
        self.__imutable = False
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        self.__number = new_number
        
    @property
    def imutable(self):
        return self.__imutable
    
    @imutable.setter
    def imutable(self, new_imutable):
        if new_imutable == False:
            raise Exception
        self.__imutable = new_imutable
    
if __name__ == "__main__":
    ii = ImutableInteger(5)
    print(ii.number)

    ii.imutable = True
    ii.number = 60
