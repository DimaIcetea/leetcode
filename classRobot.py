# Створіть клас Робот (Robot), який рухається в заданих напрямках та записує траєкторію свого руху. 
# Координатна сітка, за якою відбувається рух робота, задається в межах осей X та Y, 
# причому додатній напрямок осі X співпадає із напрямком з півдня (s) на північ (n), осі Y – з напрямком із заходу (w) на схід (e).
# У метод ініціалізації екземпляра класу передаються тільки аргументи, що відповідають поточним координатам x та y, 
# а у тілі методу іншим атрибутам привласнюються деякі початкові значення.

class Robot:
    directions = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'n'
        self.path = [[0, 0, 'n']]
    
    def info(self):
        print(f'Поточні координати: ({self.x}, {self.y})')
        print(f'Напрямок руху: {self.direction}')
        print('Траєкторія руху:')
        for step in self.path:
            print(f'({step[0]}, {step[1]}, {step[2]})')
    
    def move(self):
        dx, dy = Robot.directions[self.direction]
        new_x, new_y = self.x + dx, self.y + dy
        if self.is_valid_position(new_x, new_y):
            self.x, self.y = new_x, new_y
            self.path.append([self.x, self.y, self.direction])
        else:
            print('Неможливо виконати хід - робот вийде за межі допустимої області.')
    
    def turn_right(self):
        self.direction = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}[self.direction]
        self.path.append([self.x, self.y, self.direction])
    
    def turn_left(self):
        self.direction = {'n': 'w', 'e': 'n', 's': 'e', 'w': 's'}[self.direction]
        self.path.append([self.x, self.y, self.direction])

    def is_valid_position(self, x, y):
        # Проверка на недопустимые значения координат
        return 0 <= x <= 10 and 0 <= y <= 10

# def info выводит все текущие координаты
# turn_rig/left поворачивают на 90 градусов
# is_valid проверяет ,находится в допустимом
# path = список всех позиций робота