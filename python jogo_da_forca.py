import random

# Lista de palavras
palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]

# Selecionar uma palavra aleatória
palavra = random.choice(palavras)
palavra = palavra.lower()  # Converter para minúsculas

# Variáveis de controle
letras_erradas = []
letras_corretas = []
tentativas = 6  # Número máximo de tentativas antes de perder o jogo

# Função para exibir a forca
def exibir_forca():
    print("  _______ ")
    print(" |/      |")
    print(" |      {0}".format("O" if len(letras_erradas) > 0 else ""))
    print(" |     {0}{1}{2}".format("/" if len(letras_erradas) > 1 else "", "|" if len(letras_erradas) > 2 else "", "\\" if len(letras_erradas) > 3 else ""))
    print(" |      {0}".format("|" if len(letras_erradas) > 4 else ""))
    print(" |     {0} {1}".format("/" if len(letras_erradas) > 5 else "", "\\" if len(letras_erradas) > 6 else ""))
    print(" |")
    print("_|___")

# Loop principal do jogo
while True:
    # Mostrar a palavra com os espaços em branco para letras não descobertas
    palavra_exibida = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    print("\nPalavra:", palavra_exibida)

    # Mostrar letras erradas
    print("Letras erradas:", letras_erradas)

    # Verificar se ganhou o jogo
    if all(letra in letras_corretas for letra in palavra):
        print("\nParabéns! Você ganhou!")
        break

    # Verificar se perdeu o jogo
    if len(letras_erradas) >= tentativas:
        print("\nVocê perdeu! A palavra era:", palavra)
        break

    # Pedir uma letra ao usuário
    letra = input("Digite uma letra: ").lower()

    # Verificar se a letra já foi digitada
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já digitou essa letra. Tente novamente!")
        continue

    # Verificar se a letra está na palavra
    if letra in palavra:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)

    # Imprimir a forca atual
    exibir_forca()