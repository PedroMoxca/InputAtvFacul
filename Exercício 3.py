print('Programinha de controle de festinha 1.0')
print('#######################################')

numero_de_convidados = input('Coloque o numero de convidados: ')
lista_de_convidados = []

i=1
while i <= int(numero_de_convidados):
    nome_de_convidado = input('Coloque o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nome_de_convidado)
    i += 1

print('Serão',numero_de_convidados, 'convidados')

print('\n LISTA DE CONVIDADOS')
for convidado in lista_de_convidados:
    print(convidado)

