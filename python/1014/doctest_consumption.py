"""
url: https://judge.beecrowd.com/pt/problems/view/1013
Author: Weder Carlos
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

 ____________________________________________________
|Exemplo de Entrada              | Exemplo de Saída  |
|--------------------------------------------------- |
|500                             | 14.286 km/l       |
|35.0                            |                   |
 ----------------------------------------------------
|2254                            | 18.119 km/l       |
|124.4                           |                   |
 ----------------------------------------------------
|4554                            | 9.802 km/l        |
|464.6                           |                   |
 ----------------------------------------------------
"""

import doctest


def consumption(x, y):
    """
    Calcula o consumo médio de um automóvel.

    :param x: int
    :param y: float
    :return: str

    >>> consumption(500, 35.0)
    '14.286 km/l'
    >>> consumption(2254, 124.4)
    '18.119 km/l'
    >>> consumption(4554, 464.6)
    '9.802 km/l'
    """
    return f'{x / y:.3f} km/l'


doctest.testmod()
