from time import sleep

# for c in range(0, 5 +1):
#     print(c)
#     sleep(1)
# print("Feliz ano novo!!!")

# while = enquanto

# cont = 10
# while cont != 0:  # Retorna true or False
#     print(cont)
#     cont = cont - 1


# par = impar = 0
# n = 1

# while parar != 0:
#   n = int(input("Digite um número: "))
#   if n % 2 == 0:
#     par = par +1
#   else :
#     impar = impar + 1

# print(f'''
#   Você digitou {par} números pares
#   E {impar} numeros impares
# ''')


# senha = ""
# while senha != "dorival26":

#     senha = str(input("Degite a senha: "))

# print("Senha correta")


senha = "dorival"
tentativas = input("Digite a senha: ")

while senha != tentativas:
    print("senha incorreta")
    tentativas = input("Digite a senha: ")
print("Seja Bem vindo ")
