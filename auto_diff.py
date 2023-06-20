import sympy as sp

x, ε, a = sp.symbols("x ε a")

class DualNumber:
    def __init__(self, real_part, dual_part):
        self.real_part = real_part
        self.dual_part = dual_part

    # 加法の定義
    def __add__(self, other):
        if isinstance(other, DualNumber):
            real = self.real_part + other.real_part
            dual = self.dual_part + other.dual_part
            return DualNumber(real, dual)
        elif isinstance(other, int) or isinstance(int, other):
            return DualNumber(self.real_part + other, self.dual_part)
        else:
            raise TypeError("Unsupported operand type for +")
        
    # 乗法の定義
    def __mul__(self, other):
        if isinstance(other, DualNumber):
            real = self.real_part * other.real_part
            dual = self.real_part * other.dual_part + self.dual_part * other.real_part
            return DualNumber(real, dual)
        elif isinstance(other, int) or isinstance(int, other):
            return DualNumber(self.real_part * other, self.dual_part * other)
        else:
            raise TypeError("Unsupported operand type for *")
        
    # 冪乗の定義
    def __pow__(self, power):
        if isinstance(power, int) or isinstance(int, power):
            real = self.real_part ** power
            dual = power * (self.real_part ** (power - 1)) * self.dual_part
            return DualNumber(real, dual)
        else:
            raise TypeError("Unsupported operand type for **")

f = x + 5
g = 2 * x + 3
print(f + g)   # 3*x + 8
print(sp.expand(f * g))   # 2*x**2 + 13*x + 15