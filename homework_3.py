class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}."
              
              f"У меня {education_text} высшее образование.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}, "
              f" я учился с Айсулуу в группе: {self.group}.  У меня {education_text} высшее образование.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}, "
              f"мое хобби: {self.hobby}. У меня {education_text} высшее образование.")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()

from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def age(self):
        day, month, year = map(int, self.__birth_date.split("."))

        today = datetime.now()
        age = today.year - year

        if(today.month, today.day) < (month, day):
            age -= 1

        return age

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}, "
              f" я учился с Айсулуу в группе: {self.group}.  У меня {education_text} высшее образование.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_text = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}, "
              f"мое хобби: {self.hobby}. У меня {education_text} высшее образование.")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
print(cl1.age)

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
print(fr1.age)






