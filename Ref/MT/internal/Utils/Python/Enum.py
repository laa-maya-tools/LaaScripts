
class EnumBase():
    
    @classmethod
    def getValues(cls):
        return [ v for k,v in cls.__dict__.items() if not((k[:2]=="__")and(k[-2:]=="__")) and (not callable(v))]
    
    @classmethod
    def getKeys(cls):
        return [ k for k,v in cls.__dict__.items() if not((k[:2]=="__")and(k[-2:]=="__")) and (not callable(v))]

    @classmethod
    def getDict(cls):
        return  dict((k,v) for k,v in cls.__dict__.items() if not((k[:2]=="__")and(k[-2:]=="__")) and (not callable(v)))

    @classmethod
    def getKeyFromValue(cls, value):
        dict = cls.getDict()
        for k, v in dict.items():
            if v == value:
                return k
        raise KeyError("Value not on enum: {}".format(value))
    