import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300)
canvas.grid(columnspan=3, rowspan=4)


#pealkiri
tere = tk.Label(root, text='Toit ühele', height=2, font=('Times 30'))
tere.grid(columnspan=3, column=0, row=0)


#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1)


#juhised
juhised = tk.Label(root, text='Toit ühele on programm, mis aitab sul lihtsalt leida retsepte täpselt nende', font='Times 14', height=2)
juhised.grid(columnspan=3, column=0, row=2)
juhised2 = tk.Label(root, text='koostisosadega, mis sul juba külmkapis olemas on.', font='Times 14', height=1)
juhised2.grid(columnspan=3, column=0, row=3)
juhised3 = tk.Label(root, text='Vajuta ALUSTA, vali koostisosad ning hakka kokkama!', font='Times 14', height=2)
juhised3.grid(columnspan=3, column=0, row=4)


#PROGRAMM
#avab valikute faili, lisab koostisosad järjendisse
def koostis():
    koostisosad = []
    fail = open('koostisosad.txt', encoding = 'utf-8')
    for rida in fail:
        koostisosad.append(rida.strip())
    fail.close()
    return koostisosad


def retseptid(valitud):
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
            for aine in valitud:
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
    valikud = []
    for el in valitud:
        valikud.append(el.lower())
    juurde = []
    a = ained[parim].strip().split(',')
    for el in a:
        if el not in valitud:
            juurde.append(el)
    b = ''
    for el in juurde:
        b = b + el + ', '
    print(parim)
    return(parim, retseptid, ained, juhis, b)


#loob valikuakna ning laseb kasutajal teha oma valiku
def tee_valik():
    browse_text.set('Sulge see aken')
    teine = tk.Tk()
    canvas = tk.Canvas(teine, width = 600, height = 300)
    canvas.grid(columnspan=3, rowspan=3)
    tekst = tk.Label(teine, text='Palun vali koostisosad: ')
    tekst.grid(column=1, row=2)
    valik = tk.Listbox(teine, selectmode = 'multiple', height=17, width=30)
    valik.grid(column=2, row=2)
    koostisosad = koostis()
    for el in koostisosad:
        valik.insert(koostisosad.index(el), el)
    jätka_btn = tk.Button(teine, text='JÄTKA', command=teine.destroy)
    jätka_btn.grid(column=1, row=3)
    valitud = []
    for i in valik.curselection():
        valitud.append(valik.get(i))
    print(valik.curselection())
    canvas = tk.Canvas(teine, width = 500, height = 50)
    canvas.grid(columnspan=3, rowspan=3)
    teine.mainloop()
    re = retseptid(valitud)
    kolmas_aken(re)

#väljastab vajaliku info kolmandas aknas
def kolmas_aken(re):
    kolmas = tk.Tk()
    canvas = tk.Canvas(kolmas, width=500, height=300)
    canvas.grid(columnspan=3, rowspan=4)
    parim = re[0]
    
    nimi = tk.StringVar()
    tekst = tk.Label(kolmas, textvariable=nimi, height=2, font=('Times 14'))
    nimi.set('Sulle sobivaim retsept on '+ str(re[1][parim]))
    tekst.grid(columnspan=3, column=0, row=0)
    
    ained = tk.StringVar()
    tekst2 = tk.Label(kolmas, textvariable=ained, height=2, font=('Times 12'))
    ained.set('Selleks on vaja: '+re[2][parim])
    tekst2.grid(columnspan=3, column=0, row=1)
    
    juhis = tk.StringVar()
    tekst3 = tk.Label(kolmas, textvariable=juhis, height=6, font=('Times 12'), wraplength=600)
    juhis.set(re[3][parim])
    tekst3.grid(columnspan=3, column=0, row=2)
    
    kolmas.mainloop()
    

#alusta nupp
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=lambda:tee_valik(), textvariable=browse_text, font='Times 14', bg='#82C3EC', fg='#1C315E', height=3, width=20)
browse_text.set('ALUSTA')
browse_btn.grid(column=1, row=5)


#lisab alla ruumi juurde
canvas = tk.Canvas(root, width = 500, height = 50)
canvas.grid(columnspan=3, rowspan=3)
root.mainloop()