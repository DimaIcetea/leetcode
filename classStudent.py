from datetime import datetime

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"Студент {self.name}, {self.age} років")
        
    def remains(self):
        years_left = 0
        if self.age < 17:
            years_left = 17 - self.age
        elif self.age < 22:
            years_left = 22 - self.age
        print(f"Залишилося навчатись {years_left} років")

class Bachelor(Student):
    def __init__(self, name, age, year, topic):
        super().__init__(name, age)
        self.year = year
        self.topic = topic
        
    def info(self):
        super().info()
        print(f"Тема дипломного проекту для бакалавра: {self.topic}")
        
    def remains(self):
        current_year = datetime.now().year
        years_left = current_year - self.year
        if years_left < 4:
            print(f"Залишилося навчатись {4 - years_left} років")
        else:
            print("Вже випустився")

class Master(Student):
    def __init__(self, name, age, year, topic):
        super().__init__(name, age)
        self.year = year
        self.topic = topic
        
    def info(self):
        super().info()
        print(f"Тема магістерської дисертації: {self.topic}")
        
    def remains(self):
        current_year = datetime.now().year
        years_left = current_year - self.year
        if years_left < 2:
            print(f"Залишилося навчатись {2 - years_left} років")
        else:
            print("Вже випустився")

class PhDStudent(Student):
    def __init__(self, name, age, year, topic):
        super().__init__(name, age)
        self.year = year
        self.topic = topic
        
    def info(self):
        super().info()
        print(f"Тема дисертації PhD: {self.topic}")
        
    def remains(self):
        current_year = datetime.now().year
        years_left = current_year - self.year
        if years_left < 4:
            print(f"Залишилося навчатись {4 - years_left} років")
        else:
            print("Вже випустився")

def give_diploma(student):
    if isinstance(student, Bachelor):
        print(f"{student.name} отримує диплом бакалавра")
    elif isinstance(student, Master):
        print(f"{student.name} отримує диплом магістра")
    elif isinstance(student, PhDStudent):
        print(f"{student.name} отримує диплом доктора філософії")

