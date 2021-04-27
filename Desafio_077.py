# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


a = round(20.5)
b = round(19.5)
print(a,b)

palavras = ("MERCADO", "PROGRAMAR", "DESENVOLVIMENTO", "PYTHON", "CHUPETA", "GAFANHOTO")
for x in palavras:
    print(f"\nNa palavra {x} temos ", end="")
    for letra in x:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=" ")


