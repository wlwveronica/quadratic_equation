import pytest
from quadratic_solver.quadratic import QuadraticEquation


def test_discriminant():
    eq = QuadraticEquation(1, -3, 2)
    assert eq.discriminant() == 1

def test_two_roots():
    eq = QuadraticEquation(1, -3, 2)
    roots = sorted(eq.solve())
    assert roots == [1.0, 2.0]
    assert eq.solution_category() == "Dva reálné kořeny"

def test_one_root():
    eq = QuadraticEquation(1, 2, 1)
    roots = eq.solve()
    assert roots == [-1.0]
    assert eq.solution_category() == "Jeden reálný kořen"

def test_no_real_solution():
    eq = QuadraticEquation(1, 0, 1)
    assert eq.solve() == []
    assert eq.solution_category() == "Žádné reálné řešení"

def test_a_zero():
    import pytest
    with pytest.raises(ValueError):
        QuadraticEquation(0, 2, 1)
