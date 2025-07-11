"""
Exercício 3 - Calculando a média de uma lista

Escreva uma funcao chamada `calcular_media` (sem acento) que recebe uma lista com numeros
e retorne a média dos valores dela.

Exemplo de uso:
>>> print(calcular_media([0, 100, 200]))
>>> 100
"""

def calcular_media(lista_de_numeros):
  if lista_de_numeros == []:
    return 0
  else:
    return sum(lista_de_numeros) / len(lista_de_numeros)
