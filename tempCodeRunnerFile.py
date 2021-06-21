from random import sample
perguta = int(input("Quantos jogos você quer que crie ?"))
for c in range(perguta):
    print(sorted(sample(range(1, 60), 6)))