rendszamok = []
sebessegek = []

db = 0
while len(rendszamok) < 10:
    rsz = input(f'{db + 1}. autó rendszám: ')
    if rsz == '': break
    rendszamok.append(rsz)
    sebessegek.append(int(input(f'{db + 1}. autó sebessége: ')))
    db += 1

gyorshajtok_rsz = []
gyorshajtok_seb = []

for i in range(len(sebessegek)):
    if sebessegek[i] > 90:
        gyorshajtok_rsz.append(rendszamok[i])
        gyorshajtok_seb.append(sebessegek[i])

if len(gyorshajtok_seb) > 0:
    print('gyorshajtók:')
    for i in range(len(gyorshajtok_rsz)):
        print(f'{gyorshajtok_rsz[i]}: {gyorshajtok_seb[i]} kmph')
else:
    print('nem volt gyorshajtó! yey! :3 <3 :)')



