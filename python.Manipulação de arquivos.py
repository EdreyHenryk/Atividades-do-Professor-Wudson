arquivo = open('arquivo.txt', 'a')

novo_texto = "\nEste é um novo texto adicionado ao arquivo."
arquivo.write(novo_texto)


arquivo.close()


arquivo = open('arquivo.txt', 'r')


novo_conteudo = arquivo.read()
print(novo_conteudo)


arquivo.close()