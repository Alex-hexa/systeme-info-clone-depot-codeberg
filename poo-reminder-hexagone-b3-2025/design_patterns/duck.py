class DuckMother:

    _children = []

    def __init__(self, name):
        self.__name = name

if __name__ == '__main__':
    daisy = DuckMother('daisy')
    daisy._children.append('rifi')
    daisy._children.append('fifi')
    other = DuckMother('other')
    other._children = []
    daisy._children.append('loulou')
    picsou = DuckMother('picsou')

    print('picsou', picsou._children)
    print('daisy', daisy._children)
    print('other', other._children)