import time

#Encontrar o maior valor na lista - exemplo 1
list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = list[0]#recebeu o numero 17

for i in range(1, len(list)):
    if list[i] > maior_numero:
        maior_numero = list[i]
print("O maior número da lista é:", maior_numero)        


#exemplo2
my_list = [17, 3, 11, 5, 1, 9, 15, 18]
maior = my_list[0]
for i in my_list:
     if i > maior:
        maior = if
print("Maior valor 2:", maior)

#Exemplo3
ultima_lista = my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
     mel = i
print("Maior valor 3:", mel)

#Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maça", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = false

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado == True 

    break

if achado:
    print("Elemento encontrado no índice:", i)
    else:
        print("NÃO ENCONTRADO!!!")

time.sleep(3)