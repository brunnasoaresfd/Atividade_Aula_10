def maior_de_tres(a,b,c):
    maior = a 

    if b > maior:
        maior = b 

    if c > maior:
        maior = c 

    return (maior)

print(maior_de_tres(3,9,5))
print(maior_de_tres(10,2,7))
print(maior_de_tres(1,4,8))
print(maior_de_tres(5,5,5))
print(maior_de_tres(-3,-1,-2))
    