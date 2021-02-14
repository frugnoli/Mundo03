# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até dez. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.
t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input("Digite um número entre 0 e 10: "))
    if 0 <= num <= 10:
        break
    print("Tente novamente. ", end='')
print(f"Você digitou o número {t[num]}.")