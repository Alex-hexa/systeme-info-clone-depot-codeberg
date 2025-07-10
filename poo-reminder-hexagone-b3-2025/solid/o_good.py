from abc import ABC, abstractmethod

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):

    @abstractmethod
    def save(self, person):
        pass

class PersonStorageDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')

class PersonStorageJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')

class PersonStorageXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a XML file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonStorageJSON()
    storage.save(person)