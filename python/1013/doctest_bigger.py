"""
url: https://judge.beecrowd.com/pt/problems/view/1013
Author: Weder Carlos
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
MaiorAB = (a + b + abs(a - b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

 ____________________________________________________
|Exemplo de Entrada              | Exemplo de Saída  |
|--------------------------------------------------- |
|7 14 106                        | 106 eh o maior    |
 ----------------------------------------------------
|217 14 6                        | 217 eh o maior    |
 ----------------------------------------------------
"""

import doctest


def maior(a, b):
    """
    Retorna o maior valor entre dois inteiros usando a fórmula:
    (a + b + abs(a - b)) // 2

    >>> maior(7, 14)
    14
    >>> maior(14, 106)
    106
    >>> maior(217, 14)
    217
    >>> maior(14, 6)
    14
    """
    return (a + b + abs(a - b)) // 2


def maior_de_tres(a, b, c):
    """
    Retorna o maior entre três valores inteiros, usando a função maior.

    :param a: int
    :param b: int
    :param c: int
    :return: str

    >>> maior_de_tres(7, 14, 106)
    '106 eh o maior'
    >>> maior_de_tres(217, 14, 6)
    '217 eh o maior'
    """
    return f'{maior(maior(a, b), c)} eh o maior'


doctest.testmod()
