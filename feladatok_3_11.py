lista = []
for i in range(40):
    lista.append((i * i) % 6)

print(lista)

paros_db = 0
for e in lista:
    if e % 2 == 0:
        paros_db += 1

if paros_db < len(lista) - paros_db:
    print('páratlan van több')
elif paros_db > len(lista) - paros_db:
    print('páros van több')
else:
    print('ugyanannyi páros és páratlan szám van')