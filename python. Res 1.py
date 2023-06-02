def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_total = custo + imposto
    return custo_total


taxa = 10  
valor = 100  
custo_total = somaImposto(taxa, valor)
print("Custo total com imposto:", custo_total)
