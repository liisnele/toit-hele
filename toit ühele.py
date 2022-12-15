import easygui
projekt = 'Toit ühele'
küsimus = 'Millised asjad leiduvad su külmkapis?'

#avab valikute faili, lisab koostisosad järjendisse
koostisosad = []
fail = open('koostisosad.txt', encoding = 'utf-8')
for rida in fail:
    koostisosad.append(rida.strip())
fail.close()

#küsib kasutajalt valikud, kui ei vali, väljastab teate
valik = easygui.multchoicebox(küsimus, projekt, koostisosad)

if valik == None:
    easygui.msgbox('Palun vali midagi.')


#avab retseptide faili, leiab retseptid(nende nime ja koostise) ja juhised, lisab need õigetesse järjenditesse
fail2 = open('retseptid.txt', encoding = 'utf-8')
kokku = 0
kõik = []
retseptid = []
ained = []
juhis = []
for rida in fail2:
    if rida.startswith('Retsept:'):
        rida1 = rida.strip('Retsept: ')
        rida2 = rida1.split(',')
        nimi = rida2[0]
        retseptid.append(nimi)
        koostis1 = rida2[1:]
        koostis2 = str(','.join(koostis1))
        ained.append(koostis2)
        for aine in valik:
            if aine.lower() in koostis1:
                kokku = kokku + 1
        kõik.append(kokku)
    if rida.startswith('Kuidas:'):
        rida3 = rida.strip('Kuidas: ')
        juhis.append(rida3)
fail2.close()


#leiab suurima sobivate asjade arvuga retsepti
suurim = max(kõik)
parim = kõik.index(suurim)


#leiab toiduained, mis on puudu
valitud = []
for el in valik:
    valitud.append(el.lower())

juurde = []
a = ained[parim].strip().split(',')

for el in a:
    if el not in valitud:
        juurde.append(el)
b = ''
for el in juurde:
    b = b + el + ', '

#väljastab parima retsepti
easygui.msgbox('Sulle sobivaim retsept oleks '+retseptid[parim]+'.')
easygui.msgbox('Siin on see retsept: '+ ained[parim]+'\n'+'Sul on veel puudu: '+ b +'\n'+'\n'+juhis[parim]+'\n'+'\n'+'Kui see retsept sulle ei sobi, siis proovi uuesti!:)')