from math import sqrt


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def delta(self):
        return pow(self.b, 2) - 4 * self.a * self.c

    def pierwiastekDelta(self):
        if FunkcjaKwadratowa.delta(self) >= 0:
            return sqrt(self.delta())
        return -1

    def rozwiazanie(self):
        if FunkcjaKwadratowa.delta(self) < 0:
            print("Funkcja nie ma rozwiazan rzeczywistych")
        if FunkcjaKwadratowa.delta(self) > 0:
            x1 = (-self.b - FunkcjaKwadratowa.pierwiastekDelta(self)) / (2 * self.a)
            x2 = (-self.b + FunkcjaKwadratowa.pierwiastekDelta(self)) / (2 * self.a)
            print(f"Rozwiazania rownania to x1 = {x1}, a x2 = {x2}")

        if FunkcjaKwadratowa.delta(self) == 0:
            x1 = -self.b / (2 * self.a)
            print(f"Rozwiazania rownania to x = {x1}")


rownanie1 = FunkcjaKwadratowa(1, 2, -3)

print(rownanie1.delta())
print(rownanie1.pierwiastekDelta())
rownanie1.rozwiazanie()
FunkcjaKwadratowa(2, -5, 3).rozwiazanie()
FunkcjaKwadratowa(2, 1, 3).rozwiazanie()

# def rozwiazania(self):
#
# if (delta < 0):
