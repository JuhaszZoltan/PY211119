# 12 elemű szám lista
# minden elemét beolvasni billrőr
# napi átlag meghatározása
# hány napon volt több, mint az átlag

atutalasok = []

for n in range(12):
    atutalasok.append(int(input(f'{n + 1}. napi átautalások száma: ')))

atutalasok_atlaga = sum(atutalasok) / len(atutalasok)

print(f'nappi átutalások átlaga: {atutalasok_atlaga}')

c = 0

for n in atutalasok:
    if n > atutalasok_atlaga:
        c += 1

print(f'{c} nap volt az átlagosnál nagyobb forgalom')