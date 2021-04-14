import pytest

from notas import Notas

def test_notas_maior_que_zero_np1enp2():
    notas = Notas(2,50)
    assert (notas.p1 >= 0, "values has to be positive")

def test_notas_maior_que_zero_np1enp2enp3():
    notas = Notas(30,50, 2)
    assert ((notas.p1 >= 0) and (notas.p2 >= 0) and (notas.p3 >= 0)), "values has to be positive"

def test_np1enp3_diferente_none():
    notas = Notas(1,1)
    assert not ((notas.p1 == None) or (notas.p2 == None)), "p1 and p2 shouldn't be None"

def test_aprovado_sem_np3():
    notas = Notas(59,60)
    assert notas.is_aprovado(), "average should be >= 60"

def test_aprovado_com_np3():
    notas = Notas(49,50,49)
    assert notas.is_aprovado(), "average should be >= 50"

def test_reprovado_sem_np3():
    notas = Notas(29,29)
    print(notas.is_aprovado())
    assert notas.is_aprovado() == False, "average should be <= 30"

def test_reprovado_com_np3():
    notas = Notas(49,49,49)
    assert not notas.is_aprovado(), "average should be < 50"


#pytest.mark.parametrize("inicial,final", [(0,0),(1,0),(2,1)])

#pytest --cov=notas ./src