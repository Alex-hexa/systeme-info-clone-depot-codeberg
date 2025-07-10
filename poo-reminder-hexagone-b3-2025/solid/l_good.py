from abc import ABC, abstractmethod

class Contact:

    def __init__(self, phone, email):
        self.email = email
        self.phone = phone

class Notification(ABC):

    def __init__(self, message):
        self.message = message

    @abstractmethod
    def notify(self):
        pass


class Email(Notification):

    def __init__(self, message, contact : Contact):
        super().__init__(message)
        self.contact = contact

    def notify(self):
        print(f'Send {self.message} to email {self.contact.email}')

class SMS(Notification):

    def __init__(self, message, contact):
        super().__init__(message)
        self.contact = contact

    def notify(self):
        print(f'Send {self.message} to phone {self.contact.phone}')

if __name__ == '__main__':
    notification = SMS('Hello', Contact('010101', 'gael@argonaultes.fr'))
    notification.notify()
    notification.notify()

