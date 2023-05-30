import random

# definir placar de pontos

pontos_jogador = 0
pontos_maquina = 0


def pontos():
    print("----------PLACAR----------")
    print("JOGADOR     X    MAQUINA")
    print(f"   {pontos_jogador}        X       {pontos_maquina}")

# definir opcoes de jogador


def opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura? ")
    if esc_jogador in ["Pedra", "Papel", "Tesoura"]:
        return esc_jogador
    else:
        print("Opcão inválida. Tente novamente")
        return opcao_jogador()

# definir da maquina


def opcao_maquina():
    esc_maquina = random.choice(["Pedra", "Papel", "Tesoura"])
    return esc_maquina

# Loop do jogo


while True:
    jogador = opcao_jogador()
    maquina = opcao_maquina()

# jogador vence

    if (jogador == "Pedra" and maquina == "Tesoura")\
        or (jogador == "Papel" and maquina == "Pedra")\
            or (jogador == "Tesoura" and maquina == "Papel"):
        print(f"jogador: {jogador}")
        print(f"maquina: {maquina}")
        print("VOCÊ GANHOU!")
        pontos_jogador += 1

# jogo empata

    elif jogador == maquina:
        print(f"jogador: {jogador}")
        print(f"maquina: {maquina}")
        print("EMPATE!")

# maquina vence

    else:
        pontos_maquina += 1
        print(f"jogador: {jogador}")
        print(f"maquina: {maquina}")
        print("VOCÊ PERDEU!")


# definir loop do jogo
    jogar_novamente = input("Jogar mais uma vez? (SIM ou NÃO): ")
    if jogar_novamente.lower() == "sim":
        continue  # Continua o loop sem chamar opcao_jogador() novamente
    else:
        pontos()
        print("Goodbye!")
        break
