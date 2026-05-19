class Money:
    def __init__(self, rub, cop):
        self.rub = rub
        self.cop = cop
    def __str__(self):
        return f"{self.rub}rub {self.cop}cop"
    def __add__(self, other):
        result =  Money(self.rub + other.rub, self.cop + other.cop)
        while result.cop >= 100:
            result.cop -= 100
            result.rub += 1
        return result
    def __sub__(self,other):
        result = Money(self.rub - other.rub, self.cop - other.cop)
        if self.cop <= other.cop:
            result.cop *= -1
        return result


money_sum1 = Money(10, 30)
money_sum2 = Money(20, 60)
print(money_sum1)
money_result = money_sum1 - money_sum2
print(money_result)
        
