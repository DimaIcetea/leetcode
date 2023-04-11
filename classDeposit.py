class Deposit:
    def __init__(self, name, surname, money, term, rate):
        self.name = name
        self.surname = surname
        self.money = money
        self.term = term
        self.rate = rate
    
    def info(self):
        print(f"Власник депозиту: {self.name} {self.surname}")
        print(f"Сума на депозиті: {self.money} грн")
        print(f"Термін депозиту: {self.term} місяців")
        print(f"Відсоткова ставка: {self.rate}%")
    
    def net_profit(self, ptype='simple'):
        if ptype == 'simple':
            profit = self.money * self.term * self.rate / 100 / 12
        elif ptype == 'complex':
            profit = self.money * (1 + self.rate / 100 / 12) ** (self.term) - self.money
        else:
            print("Ви ввели некоректне значення параметру ptype.")
            return None
        return profit
    
    def tax(self):
        profit = self.net_profit()
        tax_amount = profit * 0.03
        if tax_amount < 40:
            tax_amount = 40
        return tax_amount

# Метод info() друкує інформацію про власника депозиту, суму грошей, строк та відсоткову ставку.
#Метод net_profit(ptype='simple') дозволяє визначити чистий дохід за депозитом (без урахування податку) на основі атрибутів money,
# term та rate. Параметр ptype задає формулу розрахунку доходу і може приймати значення 'simple' або 'complex'. 
# Значення 'simple' використовує формулу простих відсотків, а значення 'complex' - формулу складних відсотків. 
# Значення параметру ptype за замовчуванням - 'simple'.
# Метод tax() дозволяє визначити суму податку, що складає 3% від суми доходу за депозитом, але не менше ніж 40 грн.