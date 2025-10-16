import click
from quadratic_solver.quadratic import QuadraticEquation

VERSION = "1.0.0"
AUTHOR = "Veronika Bernardova"
DATE = "09.10.2025"

@click.command()
@click.version_option(
    version=VERSION,
    message=f"Kvadratický řešitel v{VERSION} | Autor: {AUTHOR} | Datum: {DATE}"
)
@click.option('--a', type=float, required=True, help='Koeficient a')
@click.option('--b', type=float, required=True, help='Koeficient b')
@click.option('--c', type=float, required=True, help='Koeficient c')
def solve_quadratic(a, b, c):
    """Řeší kvadratickou rovnici ax² + bx + c = 0 v oboru reálných čísel."""
    try:
        eq = QuadraticEquation(a, b, c)
        roots = eq.solve()
        category = eq.solution_category()
        click.echo(f"Kategorie řešení: {category}")
        if roots:
            for i, root in enumerate(roots, start=1):
                click.echo(f"x{i} = {root}")
        else:
            click.echo("Žádné reálné kořeny.")
    except ValueError as e:
        click.echo(f"Chyba: {e}")

if __name__ == "__main__":
    solve_quadratic()
