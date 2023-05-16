import random

class Rating:
    def __init__(self):
        self.__exams = [random.randint(20, 100) for _ in range(random.randint(4, 7))]
        self.__pass = [random.randint(20, 100) for _ in range(random.randint(4, 7))]

    @property
    def exams(self):
        return self.__exams

    @property
    def pass_marks(self):
        return self.__pass

    @exams.setter
    def exams(self, new_exams):
        if input("Введіть пароль: ") == "illa":
            self.__exams = [mark if mark > 60 else 60 for mark in new_exams]
        else:
            print("Невірний пароль.")

    @pass_marks.setter
    def pass_marks(self, new_pass_marks):
        if input("Введіть пароль: ") == "illa":
            self.__pass = [mark if mark > 60 else 60 for mark in new_pass_marks]
        else:
            print("Невірний пароль.")

    def calculate_average(self):
        if all(mark > 60 for mark in self.__exams + self.__pass):
            average = sum(self.__exams + self.__pass) / (len(self.__exams) + len(self.__pass))
            return average
        else:
            retake_count = sum(mark <= 60 for mark in self.__exams + self.__pass)
            return retake_count

# Приклад використання класу:
rating = Rating()
print("Екзамени:", rating.exams)
print("Оцінки:", rating.pass_marks)

rating.exams = [80, 75, 90, 55]  # Зміна оцінок за екзамени
rating.pass_marks = [70, 65, 50, 85]  # Зміна оцінок за заліки

print("Екзамени:", rating.exams)
print("Оцінки:", rating.pass_marks)

average = rating.calculate_average()
if isinstance(average, int):
    print("Ви повинні перездати", average, "екзаменів або отримати задовільні оцінки.")
else:
    print("Середній бал:", average)
