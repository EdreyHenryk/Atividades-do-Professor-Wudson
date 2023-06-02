arquivo = open('arquivo.txt', 'r')


conteudo = arquivo.read()

quantidade_caracteres = len(conteudo)


print("O arquivo possui", quantidade_caracteres, "caracteres.")


arquivo.close()
