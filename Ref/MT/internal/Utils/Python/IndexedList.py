class IndexedList(object):
    def __init__(self, listValues):
        self.__values = []
        self.__indexes = []
        
        for item in listValues:
            if (len(item) == 2):
                if (type(item[1]) == int):
                    self.__values.append(item[0])
                    self.__indexes.append(item[1])
                else:
                    raise Exception("Index element is not an Integer: {}".format(item[1]))
            else:
                raise Exception('Indexed Item has invalid number of elements: {}'.format(item))
    
    def __iter__(self):
        self.iterN = 0
        return self
    
    def __next__(self):
        if (self.iterN < len(self.__values)):
            result = (self.__values[self.iterN], self.__indexes[self.iterN])
            self.iterN += 1
            return result
        else:
            raise StopIteration
    
    def values(self):
        return self.__values
    
    def indexes(self):
        return self.__indexes
    
    def indexOf(self, val):
        try:
            auxIdx = self.__values.index(val)
            return self.__indexes[auxIdx]
        except:
            raise Exception("Value is not in IndexedList: {}".format(val))
    
    def valueOf(self, val):
        try:
            auxIdx = self.__indexes.index(val)
            return self.__values[auxIdx]
        except:
            raise Exception("Index is not in IndexedList: {}".format(val))
    
    def positionOfValue(self, val):
        try:
            return self.__values.index(val)
        except:
            raise Exception("Value is not in IndexedList: {}".format(val))
    
    def positionofIndex(self, val):
        try:
            return self.__indexes.index(val)
        except:
            raise Exception("Index is not in IndexedList: {}".format(val))
    
    def valueOfPosition(self, pos):
        return self.__values[pos]
    
    def indexOfPosition(self, pos):
        return self.__indexes[pos]
    
    def count(self):
        return len(self.__values)