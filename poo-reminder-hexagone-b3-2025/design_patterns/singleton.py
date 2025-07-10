class Duck:

    _duck = None

    def __new__(cls, color: str):
        if cls._duck is None:
            cls._duck = object.__new__(cls)
        return cls._duck

    def __init__(self, color: str):
        self.__color = color #dunder

    @classmethod
    def get_instance(cls, color: str):
        if cls._duck is None:
            cls._duck = Duck(color)
        return cls._duck

    def __repr__(self) -> str:
        return f'duck: {self.__color}'

if __name__ == '__main__':
    #TODO: always get the same ref Duck
    donald = Duck.get_instance('yellow')
    foufou = Duck('red')
    riri = Duck.get_instance('blue')
    another = Duck.get_instance('red')
    print(donald)
    print(riri)
    print(another)
    assert donald == riri
    assert donald == another
    assert foufou == donald
    
