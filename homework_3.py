class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation  # Приватный атрибут
        self.__higher_education = higher_education  # Приватный атрибут
    
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


# Проверка работы кода
if __name__ == "__main__":
    cll = Classmate('Иван', '20.02.2000', 'СТУДЕНТ', True, 'ILD')
    cll.introduce()  # Привет, меня зовут Иван. Моя профессия студент. Я учился с Айсу
    
    frl = Friend('Айбек', '20.02.2000', 'СТУДЕНТ', True, 'футбол')
    frl.introduce()  # Привет, меня зовут Айбек. Моя профессия студент. Мое хобби футбол
