import pytest
import calculadora_subsidio_ferias as csf


def test_salario_hora_string_is_number():
    with pytest.raises(TypeError):
        csf.salario_hora("a", 40)


def test_salario_hora_number_is_number():
    csf.salario_hora(1000, 40)


def test_salario_hora_negative_number_is_greater_than_zero():
    with pytest.raises(ValueError):
        csf.salario_hora(-2, 40)


def test_salario_hora_zero_is_greater_than_zero():
    with pytest.raises(ValueError):
        csf.salario_hora(0, 40)


def test_horas_semanais_hora_string_is_number():
    with pytest.raises(TypeError):
        csf.salario_hora(1000, "a")


def test_horas_semanais_number_is_number():
    csf.salario_hora(1000, 40)


def test_horas_semanais_negative_number_is_greater_than_zero():
    with pytest.raises(ValueError):
        csf.salario_hora(1000, -2)


def test_horas_semanais_zero_is_greater_than_zero():
    with pytest.raises(ValueError):
        csf.salario_hora(1000, 0)


def test_horas_semanais_169_is_less_or_equal_to_168():
    with pytest.raises(ValueError):
        csf.salario_hora(1000, 169)


def test_horas_semanais_168_is_less_or_equal_to_168():
    csf.salario_hora(1000, 168)


def test_horas_semanais_167_is_less_or_equal_to_168():
    csf.salario_hora(1000, 167)


def test_salario_hora_calcula():
    salario = 1000
    horas_semanais = 40

    salario_hora = (1000 / 40) * (12 / 52)
    salario_hora_calculado = csf.salario_hora(1000, 40)

    assert salario_hora == salario_hora_calculado
