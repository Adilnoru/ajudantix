def salario_hora(salario, horas_semanais):
    verifica_valor_valido(salario, '"salário"')
    verifica_valor_valido(horas_semanais, '"horas_semanais"', 168)
    return (salario / horas_semanais) * (12 / 52)


def verifica_valor_valido(valor, nome, limite_superior=None):
    if type(valor) is not (int or float):
        raise TypeError("O valor {} tem que ser um número!".format(nome))
    if valor <= 0:
        raise ValueError("O valor {} tem que ser maior que zero!".format(nome))
    if limite_superior:
        if valor > limite_superior:
            raise ValueError(
                "O valor {} tem que ser menor que {}".format(nome, limite_superior)
            )
