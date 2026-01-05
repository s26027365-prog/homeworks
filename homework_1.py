class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"

        introduction = (
            f"меня зовут {self.name}, я родился {self.birth_date},"
            f"по профессии {self.occupation}, высшего образования {education_text}"
        )

        return introduction

person1 = Person("Тилль Линдеман", "4.01.1963", "корзинщик", False)
person2 = Person("Курт Кобейн", "20.02.1967", "музыкант", False)
person3 = Person("Браен Мэй","19.07.1947", "астрофизик", True)

print("=" * 50)
print("Атрибуты экземпляров класса Person:")
print("=" * 50)

persons = [person1, person2, person3]

for i, person in enumerate(persons, 1):
    print(f"\nЭкземпляр {i}:")
    print(f"  Имя: {person.name}")
    print(f"  Дата рождения: {person.birth_date}")
    print(f"  Профессия: {person.occupation}")
    print(f"  Высшее образование: {person.higher_education}")

print("\n" + "=" * 50)
print("Представление каждого экземпляра:")
print("=" * 50)

# Вызываем метод introduce для каждого экземпляра
for i, person in enumerate(persons, 1):
    print(f"\nЭкземпляр {i}:")
    print(person.introduce())
print("=" * 50)
