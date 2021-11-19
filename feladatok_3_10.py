import random as rnd

nevek = ['Zoli', 'Béla', 'Ákos', 'Tamás', 'Emese']
orak = []

for n in range(len(nevek)):
    orak.append(rnd.randint(0, 9))

avg = sum(orak) / len(orak)
print(f'internetezéssel töltött órák átlaga: {avg} óra')

c = 0
for o in orak:
    if o >= 2:
        c += 1
print(f'{c} diák internetezik 2 óránál többet naponta')

print(nevek)
print(orak)

i = 0
while i < len(orak) and orak[i] != 0:
    i += 1
if i < len(orak):
    print('van olyan diák, aki egyáltalán nem internetezik')
    print(f'az ő neve: {nevek[i]}')
else:
    print('minden diák interneteziki valamennyit')

# fügvénnyel ugyan ez:
# van_olyan_aki_nem_internetezik = orak.__contains__(0)

if orak.__contains__(0):
    print('van olyan aki nem internetezik')
else:
    print('mindenki internetezik valamennyit')