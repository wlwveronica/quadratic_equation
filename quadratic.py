import math
import sys

class QuadraticEquation:
    def __init__(self, a: float, b: float, c: float):
        if a == 0:
            raise ValueError("Koeficient a nesmí být 0 – nejedná se o kvadratickou rovnici.")
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        d = self.discriminant()
        if d < 0:
            return []
        elif d == 0:
            x = -self.b / (2 * self.a)
            return [x]
        else:
            sqrt_d = math.sqrt(d)
            x1 = (-self.b + sqrt_d) / (2 * self.a)
            x2 = (-self.b - sqrt_d) / (2 * self.a)
            return [x1, x2]

    def solution_category(self) -> str:
        d = self.discriminant()
        if d < 0:
            return "Žádné reálné řešení"
        elif d == 0:
            return "Jeden reálný kořen"
        else:
            return "Dva reálné kořeny"

# ------------------------------
# Spuštění ze skriptu v terminálu
# ------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Použití: python3 rovnice.py <a> <b> <c>")
        print("Například: python3 rovnice.py 1 -3 2")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])

        equation = QuadraticEquation(a, b, c)
        roots = equation.solve()
        category = equation.solution_category()

        print("Řešení:", roots)
        print("Kategorie:", category)

    except ValueError as e:
        print("Chyba:", e)
        sys.exit(1)
