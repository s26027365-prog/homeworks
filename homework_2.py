class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, "
              f"работаю {self.occupation}, высшее образование {education_text}")

        print(introduction)


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__( name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        # Свой текст, без super().introduce()
        print(f"Привет, меня зовут {self.name}, я одноклассник Байэля, "
              f"я родился {self.birth_date}, работаю {self.occupation}, "
              f"учусь в группе: {self.group}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__( name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        # Свой текст, без super().introduce()
        print(f"Привет, меня зовут {self.name}, я друг Байэля, "
              f"я родился {self.birth_date}, работаю {self.occupation}, "
              f"мое хобби: {self.hobby}")

print("=" * 50)
print("Одноклассники:")
print("=" * 50)

classmate1 = Classmate("Бектур", "5.12.2000", "программистом", True, "ИТ-21")
classmate2 = Classmate("Айбек", "15.08.2001", "тестировщиком", False, "КН-22")

classmate1.introduce()
classmate2.introduce()

print("\n" + "=" * 50)
print("Друзья:")
print("=" * 50)

friend1 = Friend("Алмаз", "5.12.2000", "программистом", True, "футбол")
friend2 = Friend("Данияр", "20.03.1999", "дизайнером", True, "фотография")

friend1.introduce()
friend2.introduce()






