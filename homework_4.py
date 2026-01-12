class Contact:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number: str) -> bool:
        digits_only = ''.join(filter(str.isdigit, phone_number))
        return len(digits_only) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name: str, phone_number: str) -> None:
        if not Contact.validate_phone_number(phone_number):
            raise ValueError(f"Некорректный номер телефона: '{phone_number}'. Должно быть ровно 10 цифр.")

        new_contact = Contact(name, phone_number)
        cls.all_contacts.append(new_contact)

    @classmethod
    def get_all_contacts(cls) -> list:
        return cls.all_contacts

    @classmethod
    def clear_all_contacts(cls) -> None:
        cls.all_contacts.clear()

    @classmethod
    def find_contact_by_name(cls, name: str):
        for contact in cls.all_contacts:
            if contact.name == name:
                return contact
        return None

    @classmethod
    def find_contact_by_phone(cls, phone_number: str):
        for contact in cls.all_contacts:
            if contact.phone_number == phone_number:
                return contact
        return None

    @classmethod
    def get_contacts_count(cls) -> int:
        return len(cls.all_contacts)


print(f"Начальное состояние: {ContactList.all_contacts}")
print(f"Количество контактов: {ContactList.get_contacts_count()}")

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

print(f"\nВсего контактов: {ContactList.get_contacts_count()}")
for contact in ContactList.all_contacts:
    print(f"{contact.name}: {contact.phone_number}")

vasya = ContactList.find_contact_by_name("Вася Пупкин")
if vasya:
    print(f"\nНайден: {vasya.name} - {vasya.phone_number}")

try:
    ContactList.add_contact("John Doe", "5551234")
    print("Контакт добавлен")
except ValueError as e:
    print(f"\nОшибка при добавлении контакта: {e}")


