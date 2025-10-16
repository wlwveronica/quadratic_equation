import math
import argparse

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


def main():
    parser = argparse.ArgumentParser(
        description="Řešení kvadratické rovnice v oboru reálných čísel."
    )
    parser.add_argument("a", type=float, nargs='?', help="Koeficient a")
    parser.add_argument("b", type=float, nargs='?', help="Koeficient b")
    parser.add_argument("c", type=float, nargs='?', help="Koeficient c")
    parser.add_argument(
        "--version", action="version",
        version="Řešení kvadratické rovnice 1.0\nAutor: Veronika Bernardová\nDatum: 2025-10-16"
    )

    args = parser.parse_args()

    if args.a is None or args.b is None or args.c is None:
        parser.print_help()
        return

    try:
        equation = QuadraticEquation(args.a, args.b, args.c)
        roots = equation.solve()
        category = equation.solution_category()

        print("Řešení:", roots)
        print("Kategorie:", category)

    except ValueError as e:
        print("Chyba:", e)


if __name__ == "__main__":
    main()
