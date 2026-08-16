import random

tentativas = 10
certo = random.randint(1, 100)

while tentativas > 0:
    numero = int(input("Digite um número entre 1 e 100: "))

    if numero == certo:
        print("Parabéns! Você acertou!")
        break

    elif numero < certo:
        tentativas -= 1
        print("O número é maior.")
        print(f"Você tem {tentativas} tentativas restantes.")

    else:
        tentativas -= 1
        print("O número é menor.")
        print(f"Você tem {tentativas} tentativas restantes.")

if tentativas == 0:
    print(f"Você perdeu! O número era {certo}.")