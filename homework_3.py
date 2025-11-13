class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    
    def introduce(self):
        education_status = "имею высшее образование" if self.__higher_education else "не имею высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. Я {education_status}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, major):
        super().__init__(name, birth_date, occupation, higher_education)
        self.major = major
    
    def introduce(self):
        education_status = "имею высшее образование" if self._Person__higher_education else "не имею высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self._Person__occupation}. Я {education_status}. Я учился с Айсу")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    
    def introduce(self):
        education_status = "имею высшее образование" if self._Person__higher_education else "не имею высшего образования"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self._Person__occupation}. Я {education_status}. Мое хобби {self.hobby}")


cll = Classmate('Иван', '20.02.2000', 'СТУДЕНТ', True, 'ILD')
cll.introduce()

frl = Friend('Айбек', '20.02.2000', 'СТУДЕНТ', True, 'футбол')
frl.introduce()
