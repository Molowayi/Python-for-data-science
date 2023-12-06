class Calculator:
    def __init__(self) -> None:
        self.result = 0
        self.size ="L"
        self.numer_of_TOTO = 4
        self.brand = "HP"
    def add(self):
        self.result +=1
calc = Calculator() # appelle __init__
calc2 = Calculator()
print(calc.result)
print(calc2.result)
calc.add()          # appelle add
print(calc.result)
print(calc2.result)
