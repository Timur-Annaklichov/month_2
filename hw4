class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    
    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        return False


class ContactList:
    all_contacts = []
    
    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
            print(f"Контакт {name} добавлен")
        else:
            raise ValueError(f"Номер {phone_number} должен содержать ровно 10 цифр")
