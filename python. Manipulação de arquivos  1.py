arquivo = open('arquivo.txt', 'w')


frase = "Olá, mundo!"
arquivo.write(frase)


arquivo.close()


arquivo = open('arquivo.txt', 'r')


conteudo = arquivo.read()
print(conteudo)

arquivo.close()
