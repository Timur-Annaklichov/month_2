# homework_3.py

class Person:
    def __init__(self, name, age, occupation, higher_education):
        self.name = name
        self.age = age
        self.__occupation = occupation  # приватный атрибут
        self.__higher_education = higher_education  # приватный атрибут
    
    # Геттеры для приватных атрибутов
    def get_occupation(self):
        return self.__occupation
    
    def get_higher_education(self):
        return self.__higher_education
    
    def introduce(self):
        education_status = "имею" if self.__higher_education else "не имею"
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет. Я {self.__occupation} и {education_status} высшее образование.")


class Classmate(Person):
    def __init__(self, name, age, occupation, higher_education, group_name):
        super().__init__(name, age, occupation, higher_education)
        self.group_name = group_name
    
    def introduce(self):
        # Используем геттеры вместо прямого доступа к приватным атрибутам
        education_status = "имею" if self.get_higher_education() else "не имею"
        print(f"Привет! Я {self.name}, мне {self.age} лет. Я учусь в группе {self.group_name}, хочу стать {self.get_occupation()} и {education_status} высшее образование.")


class Friend(Person):
    def __init__(self, name, age, occupation, higher_education, hobby):
        super().__init__(name, age, occupation, higher_education)
        self.hobby = hobby
    
    def introduce(self):
        # Используем геттеры вместо прямого доступа к приватным атрибутам
        education_status = "имею" if self.get_higher_education() else "не имею"
        print(f"Привет! Я {self.name}, мне {self.age} лет. По профессии я {self.get_occupation()}, {education_status} высшее образование, а в свободное время люблю заниматься {self.hobby}.")


# Создаем объекты Classmate
classmate1 = Classmate("Алексей", 20, "программистом", False, "ПИ-21")
classmate2 = Classmate("Мария", 19, "дизайнером", False, "ДЗ-20")

# Создаем объекты Friend
friend1 = Friend("Иван", 25, "инженер", True, "фотографией")
friend2 = Friend("Ольга", 23, "маркетолог", True, "йогой")

# Вызываем метод introduce() у каждого объекта
print("=== Одногруппники ===")
classmate1.introduce()
classmate2.introduce()

print("\n=== Друзья ===")
friend1.introduce()
friend2.introduce()
