# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os números sorteados foram: ", end="")
for x in num:
    print(f"{x} ", end="")
print(f"\nO maior valor sorteado foi {max(num)}")
print(f"O menor valor sorteado foi {min(num)}")

