def contarDigitos(frase):
    contador = 0
    for caractere in frase:
        if caractere.isdigit():
            contador += 1
    return contador


frase = input("Digite uma frase: ")
quantidade_digitos = contarDigitos(frase)
print("Quantidade de dígitos na frase:", quantidade_digitos)
