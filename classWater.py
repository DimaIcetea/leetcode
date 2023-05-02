class Water:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        
    def calculate_params(self):
        return self.length * self.width
        
    def about(self):
        print(f"Назва водойми: {self.name}, Довжина: {self.length}, Ширина: {self.width}")
        
        
class Lake(Water):
    def __init__(self, name, length, width, depth):
        super().__init__(name, length, width)
        self.depth = depth
        
    def calculate_params(self):
        return super().calculate_params() * self.depth
        
    def about(self):
        super().about()
        print(f"Глибина: {self.depth}")
        
        
class Sea(Water):
    def __init__(self, name, length, width, depth, salinity):
        super().__init__(name, length, width)
        self.depth = depth
        self.salinity = salinity
        
    def calculate_params(self):
        return super().calculate_params() * self.depth
        
    def about(self):
        super().about()
        print(f"Глибина: {self.depth}, Солоність: {self.salinity} ‰")
        
        
class Aquatorium:
    def __init__(self, water_objects):
        self.water_objects = water_objects
        
    def fresh_salt(self):
        fresh = 0
        salt = 0
        for obj in self.water_objects:
            if isinstance(obj, Lake):
                fresh += 1
            elif isinstance(obj, Sea):
                salt += 1
        print(f"Кількість озер: {fresh}, Кількість морів: {salt}")
        
    def water_resources(self):
        total_volume = 0
        for obj in self.water_objects:
            total_volume += obj.calculate_params()
        print(f"Загальний об'єм води: {total_volume} кубічних метрів")
