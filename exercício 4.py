def maior(var):
    maior_item = var [0]
    for item in var:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(var):
    menor_item = var[0]
    for item in var:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([1,-2,1.2,87.2,9328,0,-9]))

