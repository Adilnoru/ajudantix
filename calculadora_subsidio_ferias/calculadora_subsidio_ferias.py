def salario_hora(salario, horas_semanais):
    verifica_valor_valido(salario, '"salário"')
    verifica_valor_valido(horas_semanais, '"horas_semanais"', 168)
    return (salario / horas_semanais) * (12 / 52)


def subsidio_ferias_diario(salario_hora, horas_semanais):
    verifica_valor_valido(salario_hora, "Salario Hora")
    verifica_valor_valido(horas_semanais, "Horas Semanais", 168)
    return salario_hora * ((horas_semanais * 52) / (12 * 22))


def subsidio_ferias(salario, horas_semanais, dias_ferias):
    verifica_valor_valido(dias_ferias, "Dias de férias", 22)
    salario_hora_val = salario_hora(salario, horas_semanais)
    subsidio_ferias_diario_val = subsidio_ferias_diario(
        salario_hora_val, horas_semanais
    )
    return subsidio_ferias_diario_val * dias_ferias


def verifica_valor_valido(valor, nome, limite_superior=None):
    if type(valor) is (not int) or (not float):
        raise TypeError("O valor {} tem que ser um número!".format(nome))
    if valor <= 0:
        raise ValueError("O valor {} tem que ser maior que zero!".format(nome))
    if limite_superior:
        if valor > limite_superior:
            raise ValueError(
                "O valor {} tem que ser menor que {}".format(nome, limite_superior)
            )
