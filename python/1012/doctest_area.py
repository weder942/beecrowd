"""
url: https://judge.beecrowd.com/pt/problems/view/1012
Author: Weder Carlos
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
 ____________________________________________________
|Exemplo de Entrada              | Exemplo de Saída  |
|--------------------------------------------------- |
|3.0 4.0 5.2                     | TRIANGULO: 7.800  |
|                                | CIRCULO: 84.949   |
|                                | TRAPEZIO: 18.200  |
|                                | QUADRADO: 16.000  |
|                                | RETANGULO: 12.000 |
 ----------------------------------------------------
|12.7 10.4 15.2                  | TRIANGULO: 96.520 |
|                                | CIRCULO:  725.833 |
|                                | TRAPEZIO: 175.560 |
|                                | QUADRADO: 108.160 |
|                                | RETANGULO: 132.080|
 ----------------------------------------------------
"""

import doctest


def triangle_area(base, height):
    """
    Given two floats base and height, return the area of a triangle.

    :param base: float
    :param height: float
    :return: string

    >>> triangle_area(3.0, 5.2)
    'TRIANGULO: 7.800'
    >>> triangle_area(12.7, 15.2)
    'TRIANGULO: 96.520'
    """
    return f'TRIANGULO: {(base * height) / 2:.3f}'


def circle_area(radius):
    """
    Given a float radius, return the area of a circle.

    :param radius: float
    :return: string

    >>> circle_area(5.2)
    'CIRCULO: 84.949'
    >>> circle_area(15.2)
    'CIRCULO: 725.833'
    """
    pi = 3.14159
    return f'CIRCULO: {pi * radius ** 2:.3f}'


def trapezium_area(base1, base2, height):
    """
    Given two floats base1, base2 and height, return the area of a trapezium.

    :param base1: float
    :param base2: float
    :param height: float
    :return: string

    >>> trapezium_area(3.0, 4.0, 5.2)
    'TRAPEZIO: 18.200'
    >>> trapezium_area(12.7, 10.4, 15.2)
    'TRAPEZIO: 175.560'
    """
    return f'TRAPEZIO: {((base1 + base2) * height) / 2:.3f}'


def square_area(side):
    """
    Given a float side, return the area of a square.

    :param side: float
    :return: string

    >>> square_area(4.0)
    'QUADRADO: 16.000'
    >>> square_area(10.4)
    'QUADRADO: 108.160'
    """
    return f'QUADRADO: {side ** 2:.3f}'


def rectangle_area(base, height):
    """
    Given two floats base and height, return the area of a rectangle.

    :param base: float
    :param height: float
    :return: string

    >>> rectangle_area(3.0, 4.0)
    'RETANGULO: 12.000'
    >>> rectangle_area(12.7, 10.4)
    'RETANGULO: 132.080'
    """
    return f'RETANGULO: {base * height:.3f}'


doctest.testmod()
