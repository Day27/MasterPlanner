import Tkinter as tk
import mysql.connector
import functools
import ttk

def verbind_met_GB(username,hostname,gegevensbanknaam):
    pwd="" # Dit zorgt voor een klein vakje om een paswoord in te geven.
    connection = mysql.connector.connect(host=hostname, user=username, passwd=pwd, db=gegevensbanknaam)
    return connection

def get_test_subject(connection):
    query = """
    SELECT Naam
    FROM vakken
    """

    cursor=connection.cursor()
    cursor.execute(query)

    res= cursor.fetchall()
    return res

def extraheer_uit_query(lst):
    res = []
    for el in lst:
         res.append(str(el[0]))
    return res

connection = verbind_met_GB('root','localhost','masterplanner')
options = get_test_subject(connection)
options = extraheer_uit_query(options)

def on_keyrelease(event,number):

    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = options
    else:
        data = []
        for item in options:
            if value in item.lower():
                data.append(item)

    # update data in listbox
    listbox = eval('listbox' + str(number))
    listbox_update(listbox,data)


def listbox_update(listbox,data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)

def check_semester(connection,semester,vaknaam,name):
    query = """
    SELECT Semester
    FROM vakken
    WHERE Naam=""" + "'" + str(vaknaam) + "'"

    cursor=connection.cursor()
    cursor.execute(query)
    res= cursor.fetchall()
    res = extraheer_uit_query(res)
    if (str(semester) == res[0]) or (res[0] == '0'):
        name.config(fg='black')
    else:
        name.config(fg='red')

def update_stp(vaknaam,number):
    query = """
    SELECT Studiepunten
    FROM vakken
    WHERE Naam=""" + "'" + str(vaknaam) + "'"

    cursor=connection.cursor()
    cursor.execute(query)
    res= cursor.fetchall()
    res = extraheer_uit_query(res)

    labelbox = eval('stp' + str(number))
    labelbox.config(text=res[0])

def update_proj(vaknaam,number):
    query = """
    SELECT Project
    FROM vakken
    WHERE Naam=""" + "'" + str(vaknaam) + "'"

    cursor=connection.cursor()
    cursor.execute(query)
    res= cursor.fetchall()
    res = extraheer_uit_query(res)
    if (res[0] == str(1)):
        res = 'Ja'
    else:
        res = 'Nee'

    labelbox = eval('proj' + str(number))
    labelbox.config(text=res)

def update_mond(vaknaam,number):
    query = """
    SELECT Examenvorm
    FROM vakken
    WHERE Naam=""" + "'" + str(vaknaam) + "'"

    cursor=connection.cursor()
    cursor.execute(query)
    res= cursor.fetchall()
    res = extraheer_uit_query(res)
    if ('Mondeling' not in res[0]) and ('mondeling' not in res[0]):
        res = 'Nee'
    else:
        res = 'Ja'

    labelbox = eval('mond' + str(number))
    labelbox.config(text=res)

def get_vaknaam(number):
    return eval('selectie' + str(number)).cget('text')

def update_moeilijkh1():
    num = 0
    den = 0

    for number in range(1,9):
        vaknaam = get_vaknaam(number)
        if vaknaam == 'Selecteer een vak':
            continue

        query = """
        SELECT Moeilijkheid
        FROM vakken
        WHERE Naam=""" + "'" + str(vaknaam) + "'"

        cursor=connection.cursor()
        cursor.execute(query)
        res= cursor.fetchall()
        res = extraheer_uit_query(res)
        if (res != str(0) and res != '?'):
            num = num + int(res[0])
            den = den + 1

    if (den != 0) and (num != 0):
        labelbox = moeilijkheid_berekend1
        labelbox.config(text=str(float(num)/den))

def update_moeilijkh2():
    num = 0
    den = 0

    for number in range(9,17):
        vaknaam = get_vaknaam(number)
        if vaknaam == 'Selecteer een vak':
            continue

        query = """
        SELECT Moeilijkheid
        FROM vakken
        WHERE Naam=""" + "'" + str(vaknaam) + "'"

        cursor=connection.cursor()
        cursor.execute(query)
        res= cursor.fetchall()
        res = extraheer_uit_query(res)
        if (res != str(0) and res != '?'):
            num = num + int(res[0])
            den = den + 1

    if (den != 0) and (num != 0):
        labelbox = moeilijkheid_berekend2
        labelbox.config(text=str(float(num)/den))

def update_moeilijkh3():
    num = 0
    den = 0

    for number in range(17,25):
        vaknaam = get_vaknaam(number)
        if vaknaam == 'Selecteer een vak':
            continue

        query = """
        SELECT Moeilijkheid
        FROM vakken
        WHERE Naam=""" + "'" + str(vaknaam) + "'"

        cursor=connection.cursor()
        cursor.execute(query)
        res= cursor.fetchall()
        res = extraheer_uit_query(res)
        if (res != str(0) and res != '?'):
            num = num + int(res[0])
            den = den + 1

    if (den != 0) and (num != 0):
        labelbox = moeilijkheid_berekend3
        labelbox.config(text=str(float(num)/den))

def update_moeilijkh4():
    num = 0
    den = 0

    for number in range(25,33):
        vaknaam = get_vaknaam(number)
        if vaknaam == 'Selecteer een vak':
            continue

        query = """
        SELECT Moeilijkheid
        FROM vakken
        WHERE Naam=""" + "'" + str(vaknaam) + "'"

        cursor=connection.cursor()
        cursor.execute(query)
        res= cursor.fetchall()
        res = extraheer_uit_query(res)
        if (res != str(0) and res != '?'):
            num = num + int(res[0])
            den = den + 1

    if (den != 0) and (num != 0):
        labelbox = moeilijkheid_berekend4
        labelbox.config(text=str(float(num)/den))

def update_tot1():
    tot = 0

    for number in range(1,9):
        labelbox = eval('stp' + str(number))
        tot += int(labelbox.cget('text'))

    tot_stp_berekend1.config(text=str(tot))

def update_tot2():
    tot = 0

    for number in range(9,17):
        labelbox = eval('stp' + str(number))
        tot += int(labelbox.cget('text'))

    tot_stp_berekend2.config(text=str(tot))

def update_tot3():
    tot = 0

    for number in range(17,25):
        labelbox = eval('stp' + str(number))
        tot += int(labelbox.cget('text'))

    tot_stp_berekend3.config(text=str(tot))

def update_tot4():
    tot = 0

    for number in range(25,33):
        labelbox = eval('stp' + str(number))
        tot += int(labelbox.cget('text'))

    tot_stp_berekend4.config(text=str(tot))

def update_nl():
    stp = 0
    for number in range(1,33):
        vaknaam = eval('selectie' + str(number)).cget('text')
        if (vaknaam != 'Selecteer een vak'):
            query = """
            SELECT Taal,Studiepunten,Groep
            FROM vakken
            WHERE Naam=""" + "'" + str(vaknaam) + "'"

            cursor=connection.cursor()
            cursor.execute(query)
            res= cursor.fetchall()
            if (res[0][0] == 'NL') and (res[0][2] != 'KERN'):
                stp += res[0][1]

    aantal_nl_berekend.config(text=str(stp))
    if (stp >= 10):
        aantal_nl_berekend.config(fg='green')
    else:
        aantal_nl_berekend.config(fg='black')

def update_avo():
    stp = 0
    for number in range(1,33):
        vaknaam = eval('selectie' + str(number)).cget('text')
        if (vaknaam != 'Selecteer een vak'):
            query = """
            SELECT Studiepunten,Groep
            FROM vakken
            WHERE Naam=""" + "'" + str(vaknaam) + "'"

            cursor=connection.cursor()
            cursor.execute(query)
            res= cursor.fetchall()
            if (res[0][1] == 'AVO'):
                stp += res[0][0]

    aantal_avo_berekend.config(text=str(stp))
    if (stp >= 9) and (stp <= 12):
        aantal_avo_berekend.config(fg='green')
    else:
        aantal_avo_berekend.config(fg='black')

def update_verdiepend():
    stp = 0
    for number in range(1,33):
        vaknaam = eval('selectie' + str(number)).cget('text')
        if (vaknaam != 'Selecteer een vak'):
            query = """
            SELECT Studiepunten,Groep
            FROM vakken
            WHERE Naam=""" + "'" + str(vaknaam) + "'"

            cursor=connection.cursor()
            cursor.execute(query)
            res= cursor.fetchall()
            if ('1' in res[0][1]):
                stp += res[0][0]

    aantal_verdiepend_berekend.config(text=str(stp))
    if (stp >= 24):
        aantal_verdiepend_berekend.config(fg='green')
    else:
        aantal_verdiepend_berekend.config(fg='black')

def update_bedrijven():
    stp = 0
    bedrijven = ['H03G7A', 'H02X6A', 'H0T39A', 'H0T91A']
    for number in range(1,33):
        vaknaam = eval('selectie' + str(number)).cget('text')
        if (vaknaam != 'Selecteer een vak'):
            query = """
            SELECT Code,Studiepunten
            FROM vakken
            WHERE Naam=""" + "'" + str(vaknaam) + "'"

            cursor=connection.cursor()
            cursor.execute(query)
            res= cursor.fetchall()
            if (res[0][0] in  bedrijven):
                stp += res[0][1]

    if (stp > 9):
        max_bedrijven.config(fg='red')
    else:
        max_bedrijven.config(fg='black')

def on_select(event,number,semester):
    name = eval('selectie' + str(number))
    new_text = event.widget.get('active')
    name.config(text=new_text)
    check_semester(connection,semester,new_text,name)
    update_stp(new_text,number)
    update_proj(new_text,number)
    update_mond(new_text,number)
    update_moeilijkh1()
    update_moeilijkh2()
    update_moeilijkh3()
    update_moeilijkh4()
    update_tot1()
    update_tot2()
    update_tot3()
    update_tot4()
    update_nl()
    update_avo()
    update_verdiepend()
    update_bedrijven()

def update():
    for number in range(1,6):
        vaknaam = eval('selectie' + str(number)).cget('text')
        update_stp(vaknaam,number)
        update_proj(vaknaam,number)
        update_mond(vaknaam, number)

    for number in range(9,14):
        vaknaam = eval('selectie' + str(number)).cget('text')
        update_stp(vaknaam,number)
        update_proj(vaknaam,number)
        update_mond(vaknaam, number)

    # Update vak 17
    number = 17
    vaknaam = eval('selectie' + str(number)).cget('text')
    update_stp(vaknaam,number)
    update_proj(vaknaam,number)
    update_mond(vaknaam, number)

    # Update vak 25
    number = 25
    vaknaam = eval('selectie' + str(number)).cget('text')
    update_stp(vaknaam,number)
    update_proj(vaknaam,number)
    update_mond(vaknaam, number)

    # Naamsonafhankelijke updates
    update_moeilijkh1()
    update_moeilijkh2()
    update_moeilijkh3()
    update_moeilijkh4()
    update_tot1()
    update_tot2()
    update_tot3()
    update_tot4()


# --- main ---

root = tk.Tk()
root.state('zoomed')

titel1 = tk.Label(root,text='Jaar 1, semester 1', font='Helvetica 12 bold')
titel2 = tk.Label(root,text='Jaar 1, semester 2', font='Helvetica 12 bold')
titel3 = tk.Label(root,text='Jaar 2, semester 1', font='Helvetica 12 bold')
titel4 = tk.Label(root,text='Jaar 2, semester 2', font='Helvetica 12 bold')
studiepunten1 = tk.Label(root,text='Stp', font='Helvetica 10 bold')
studiepunten2 = tk.Label(root,text='Stp', font='Helvetica 10 bold')
studiepunten3 = tk.Label(root,text='Stp', font='Helvetica 10 bold')
studiepunten4 = tk.Label(root,text='Stp', font='Helvetica 10 bold')
project1 = tk.Label(root,text='Project?', font='Helvetica 10 bold')
project2 = tk.Label(root,text='Project?', font='Helvetica 10 bold')
project3 = tk.Label(root,text='Project?', font='Helvetica 10 bold')
project4 = tk.Label(root,text='Project?', font='Helvetica 10 bold')
mondeling1 = tk.Label(root,text='Mondeling?', font='Helvetica 10 bold')
mondeling2 = tk.Label(root,text='Mondeling?', font='Helvetica 10 bold')
mondeling3 = tk.Label(root,text='Mondeling?', font='Helvetica 10 bold')
mondeling4 = tk.Label(root,text='Mondeling?', font='Helvetica 10 bold')
moeilijkheid1 = tk.Label(root,text='Gemiddelde moeilijkheid:')
moeilijkheid2 = tk.Label(root,text='Gemiddelde moeilijkheid:')
moeilijkheid3 = tk.Label(root,text='Gemiddelde moeilijkheid:')
moeilijkheid4 = tk.Label(root,text='Gemiddelde moeilijkheid:')
moeilijkheid_berekend1 = tk.Label(root,text='?')
moeilijkheid_berekend2 = tk.Label(root,text='?')
moeilijkheid_berekend3 = tk.Label(root,text='?')
moeilijkheid_berekend4 = tk.Label(root,text='?')
tot_stp1 = tk.Label(root,text='Totaal stp: ', font='Helvetica 12 bold')
tot_stp2 = tk.Label(root,text='Totaal stp: ', font='Helvetica 12 bold')
tot_stp3 = tk.Label(root,text='Totaal stp: ', font='Helvetica 12 bold')
tot_stp4 = tk.Label(root,text='Totaal stp: ', font='Helvetica 12 bold')
tot_stp_berekend1 = tk.Label(root,text='0', font='Helvetica 12 bold')
tot_stp_berekend2 = tk.Label(root,text='0', font='Helvetica 12 bold')
tot_stp_berekend3 = tk.Label(root,text='0', font='Helvetica 12 bold')
tot_stp_berekend4 = tk.Label(root,text='0', font='Helvetica 12 bold')

aantal_nl = tk.Label(root,text='Aantal keuze NL studiepunten', font='Helvetica 10 bold')
aantal_nl_berekend = tk.Label(root,text='0', font='Helvetica 10 bold')
aantal_avo = tk.Label(root,text='Aantal AVO studiepunten', font='Helvetica 10 bold')
aantal_avo_berekend = tk.Label(root,text='0', font='Helvetica 10 bold')
aantal_verdiepend = tk.Label(root,text='Aantal verdiepende studiepunten', font='Helvetica 10 bold')
aantal_verdiepend_berekend = tk.Label(root,text='0', font='Helvetica 10 bold')
max_bedrijven = tk.Label(root,text='Voorwaarde max. studiepunten stage/praktijk', font='Helvetica 10 bold')

instructies1 = tk.Label(root,text='\r Instructies:\n\rZoek OPOs in tekstvakken en selecteer.\nVak is rood als in verkeerde semester .', anchor='w', fg='blue')
instructies2 = tk.Label(root,text='Rechts worden voorwaarden gecheckt.\nGroen = genoeg; rood = te veel.', anchor='w', fg='blue')
instructies3 = tk.Label(root, text='Voor gemiddelde moeilijkheid:\nvul databank aan naar inzicht.', anchor = 'w', fg='blue')

vak1 = tk.Label(root,text='vak 1')
vak2 = tk.Label(root,text='vak 2')
vak3 = tk.Label(root,text='vak 3')
vak4 = tk.Label(root,text='vak 4')
vak5 = tk.Label(root,text='vak 5')
vak6 = tk.Label(root,text='vak 6')
vak7 = tk.Label(root,text='vak 7')
vak8 = tk.Label(root,text='vak 8')

ttk.Separator(root, orient="vertical").grid(column=9, row=0, rowspan=20, sticky='ns')
ttk.Separator(root, orient="horizontal").grid(column=0, row=25, columnspan=30, sticky='ew')
ttk.Separator(root, orient="vertical").grid(column=9, row=30, rowspan=20, sticky='ns')
ttk.Separator(root, orient="vertical").grid(column=19, row=0, rowspan=50, sticky='ns')

vak9 = tk.Label(root,text='vak 9')
vak10 = tk.Label(root,text='vak 10')
vak11 = tk.Label(root,text='vak 11')
vak12 = tk.Label(root,text='vak 12')
vak13 = tk.Label(root,text='vak 13')
vak14 = tk.Label(root,text='vak 14')
vak15 = tk.Label(root,text='vak 15')
vak16 = tk.Label(root,text='vak 16')

vak17 = tk.Label(root,text='vak 17')
vak18 = tk.Label(root,text='vak 18')
vak19 = tk.Label(root,text='vak 19')
vak20 = tk.Label(root,text='vak 20')
vak21 = tk.Label(root,text='vak 21')
vak22 = tk.Label(root,text='vak 22')
vak23 = tk.Label(root,text='vak 23')
vak24 = tk.Label(root,text='vak 24')

vak25 = tk.Label(root,text='vak 25')
vak26 = tk.Label(root,text='vak 26')
vak27 = tk.Label(root,text='vak 27')
vak28 = tk.Label(root,text='vak 28')
vak29 = tk.Label(root,text='vak 29')
vak30 = tk.Label(root,text='vak 30')
vak31 = tk.Label(root,text='vak 31')
vak32 = tk.Label(root,text='vak 32')

#entry1 = tk.Entry(root)
#entry2 = tk.Entry(root)
#entry3 = tk.Entry(root)
#entry4 = tk.Entry(root)
#entry5 = tk.Entry(root)
entry6 = tk.Entry(root)
entry7 = tk.Entry(root)
entry8 = tk.Entry(root)

#entry9 = tk.Entry(root)
#entry10 = tk.Entry(root)
#entry11 = tk.Entry(root)
#entry12 = tk.Entry(root)
#entry13 = tk.Entry(root)
entry14 = tk.Entry(root)
entry15 = tk.Entry(root)
entry16 = tk.Entry(root)

#entry17 = tk.Entry(root)
entry18 = tk.Entry(root)
entry19 = tk.Entry(root)
entry20 = tk.Entry(root)
entry21 = tk.Entry(root)
entry22 = tk.Entry(root)
entry23 = tk.Entry(root)
entry24 = tk.Entry(root)

#entry25 = tk.Entry(root)
entry26 = tk.Entry(root)
entry27 = tk.Entry(root)
entry28 = tk.Entry(root)
entry29 = tk.Entry(root)
entry30 = tk.Entry(root)
entry31 = tk.Entry(root)
entry32 = tk.Entry(root)

selectie1 = tk.Label(text="Numerieke simulatie van differentiaalvergelijkingen")
selectie2 = tk.Label(text="Technisch-wetenschappelijke software")
selectie3 = tk.Label(text="Complexe functieleer en toepassingen")
selectie4 = tk.Label(text="Systeemidentificatie en modellering")
selectie5 = tk.Label(text="Optimalisatie")
selectie6 = tk.Label(text="Selecteer een vak", fg='grey')
selectie7 = tk.Label(text="Selecteer een vak", fg='grey')
selectie8 = tk.Label(text="Selecteer een vak", fg='grey')

selectie9 = tk.Label(text="Computergestuurde regeltechniek")
selectie10 = tk.Label(text="Gevallenstudies: wiskundige ingenieurstechnieken")
selectie11 = tk.Label(text="Niet-lineaire systemen")
selectie12 = tk.Label(text="Project Wiskundige Ingenieurstechnieken")
selectie13 = tk.Label(text="Computeralgebra voor cryptografie")
selectie14 = tk.Label(text="Selecteer een vak", fg='grey')
selectie15 = tk.Label(text="Selecteer een vak", fg='grey')
selectie16 = tk.Label(text="Selecteer een vak", fg='grey')

selectie17 = tk.Label(text="Masterproef")
selectie18 = tk.Label(text="Selecteer een vak", fg='grey')
selectie19 = tk.Label(text="Selecteer een vak", fg='grey')
selectie20 = tk.Label(text="Selecteer een vak", fg='grey')
selectie21 = tk.Label(text="Selecteer een vak", fg='grey')
selectie22 = tk.Label(text="Selecteer een vak", fg='grey')
selectie23 = tk.Label(text="Selecteer een vak", fg='grey')
selectie24 = tk.Label(text="Selecteer een vak", fg='grey')

selectie25 = tk.Label(text="Masterproef")
selectie26 = tk.Label(text="Selecteer een vak", fg='grey')
selectie27 = tk.Label(text="Selecteer een vak", fg='grey')
selectie28 = tk.Label(text="Selecteer een vak", fg='grey')
selectie29 = tk.Label(text="Selecteer een vak", fg='grey')
selectie30 = tk.Label(text="Selecteer een vak", fg='grey')
selectie31 = tk.Label(text="Selecteer een vak", fg='grey')
selectie32 = tk.Label(text="Selecteer een vak", fg='grey')

stp1 = tk.Label(text = "0")
stp2 = tk.Label(text = "0")
stp3 = tk.Label(text = "0")
stp4 = tk.Label(text = "0")
stp5 = tk.Label(text = "0")
stp6 = tk.Label(text = "0")
stp7 = tk.Label(text = "0")
stp8 = tk.Label(text = "0")

stp9 = tk.Label(text = "0")
stp10 = tk.Label(text = "0")
stp11 = tk.Label(text = "0")
stp12 = tk.Label(text = "0")
stp13 = tk.Label(text = "0")
stp14 = tk.Label(text = "0")
stp15 = tk.Label(text = "0")
stp16 = tk.Label(text = "0")

stp17 = tk.Label(text = "0")
stp18 = tk.Label(text = "0")
stp19 = tk.Label(text = "0")
stp20 = tk.Label(text = "0")
stp21 = tk.Label(text = "0")
stp22 = tk.Label(text = "0")
stp23 = tk.Label(text = "0")
stp24 = tk.Label(text = "0")

stp25 = tk.Label(text = "0")
stp26 = tk.Label(text = "0")
stp27 = tk.Label(text = "0")
stp28 = tk.Label(text = "0")
stp29 = tk.Label(text = "0")
stp30 = tk.Label(text = "0")
stp31 = tk.Label(text = "0")
stp32 = tk.Label(text = "0")

proj1 = tk.Label(text = "?")
proj2 = tk.Label(text = "?")
proj3 = tk.Label(text = "?")
proj4 = tk.Label(text = "?")
proj5 = tk.Label(text = "?")
proj6 = tk.Label(text = "?")
proj7 = tk.Label(text = "?")
proj8 = tk.Label(text = "?")

proj9 = tk.Label(text = "?")
proj10 = tk.Label(text = "?")
proj11 = tk.Label(text = "?")
proj12 = tk.Label(text = "?")
proj13 = tk.Label(text = "?")
proj14 = tk.Label(text = "?")
proj15 = tk.Label(text = "?")
proj16 = tk.Label(text = "?")

proj17 = tk.Label(text = "?")
proj18 = tk.Label(text = "?")
proj19 = tk.Label(text = "?")
proj20 = tk.Label(text = "?")
proj21 = tk.Label(text = "?")
proj22 = tk.Label(text = "?")
proj23 = tk.Label(text = "?")
proj24 = tk.Label(text = "?")

proj25 = tk.Label(text = "?")
proj26 = tk.Label(text = "?")
proj27 = tk.Label(text = "?")
proj28 = tk.Label(text = "?")
proj29 = tk.Label(text = "?")
proj30 = tk.Label(text = "?")
proj31 = tk.Label(text = "?")
proj32 = tk.Label(text = "?")

mond1 = tk.Label(text = '?')
mond2 = tk.Label(text = '?')
mond3 = tk.Label(text = '?')
mond4 = tk.Label(text = '?')
mond5 = tk.Label(text = '?')
mond6 = tk.Label(text = '?')
mond7 = tk.Label(text = '?')
mond8 = tk.Label(text = '?')

mond9 = tk.Label(text = '?')
mond10 = tk.Label(text = '?')
mond11 = tk.Label(text = '?')
mond12 = tk.Label(text = '?')
mond13 = tk.Label(text = '?')
mond14 = tk.Label(text = '?')
mond15 = tk.Label(text = '?')
mond16 = tk.Label(text = '?')

mond17 = tk.Label(text = '?')
mond18 = tk.Label(text = '?')
mond19 = tk.Label(text = '?')
mond20 = tk.Label(text = '?')
mond21 = tk.Label(text = '?')
mond22 = tk.Label(text = '?')
mond23 = tk.Label(text = '?')
mond24 = tk.Label(text = '?')

mond25 = tk.Label(text = '?')
mond26 = tk.Label(text = '?')
mond27 = tk.Label(text = '?')
mond28 = tk.Label(text = '?')
mond29 = tk.Label(text = '?')
mond30 = tk.Label(text = '?')
mond31 = tk.Label(text = '?')
mond32 = tk.Label(text = '?')

titel1.grid(row = 0, columnspan = 3, sticky = 'N')
titel2.grid(row = 0, columnspan = 3, column = 10)
titel3.grid(row = 30, columnspan = 3, column = 0)
titel4.grid(row = 30, columnspan = 3, column = 10)
studiepunten1.grid(row = 0, column = 3)
studiepunten2.grid(row = 0, column = 13)
studiepunten3.grid(row = 30, column = 3)
studiepunten4.grid(row = 30, column = 13)
project1.grid(row = 0, column = 4)
project2.grid(row = 0, column = 14)
project3.grid(row = 30, column = 4)
project4.grid(row = 30, column = 14)
mondeling1.grid(row = 0, column = 5)
mondeling2.grid(row = 0, column = 15)
mondeling3.grid(row = 30, column = 5)
mondeling4.grid(row = 30, column = 15)
moeilijkheid1.grid(row = 18, column = 0)
moeilijkheid2.grid(row = 18, column = 10)
moeilijkheid3.grid(row = 48, column = 0)
moeilijkheid4.grid(row = 48, column = 10)
moeilijkheid_berekend1.grid(row = 18, column = 1)
moeilijkheid_berekend2.grid(row = 18, column = 11)
moeilijkheid_berekend3.grid(row = 48, column = 1)
moeilijkheid_berekend4.grid(row = 48, column = 11)
tot_stp1.grid(row = 18, column = 2)
tot_stp2.grid(row = 18, column = 12)
tot_stp3.grid(row = 48, column = 2)
tot_stp4.grid(row = 48, column = 12)
tot_stp_berekend1.grid(row = 18, column = 3)
tot_stp_berekend2.grid(row = 18, column = 13)
tot_stp_berekend3.grid(row = 48, column = 3)
tot_stp_berekend4.grid(row = 48, column = 13)

instructies1.grid(row = 55, sticky = 'W')
instructies2.grid(row = 56, sticky = 'W')
instructies3.grid(row = 57, sticky = 'W')

aantal_nl.grid(row = 10, column = 20)
aantal_nl_berekend.grid(row = 10, column = 21)
aantal_avo.grid(row = 11, column = 20)
aantal_avo_berekend.grid(row = 11, column = 21)
aantal_verdiepend.grid(row = 12, column = 20)
aantal_verdiepend_berekend.grid(row = 12, column = 21)
max_bedrijven.grid(row = 13, column = 20)

vak1.grid(row = 1, sticky = 'W')
vak2.grid(row = 3, sticky = 'W')
vak3.grid(row = 5, sticky = 'W')
vak4.grid(row = 7, sticky = 'W')
vak5.grid(row = 9, sticky = 'W')
vak6.grid(row = 11, sticky = 'W')
vak7.grid(row = 13, sticky = 'W')
vak8.grid(row = 15, sticky = 'W')

vak9.grid(row = 1, column = 10)
vak10.grid(row = 3, column = 10)
vak11.grid(row = 5, column = 10)
vak12.grid(row = 7, column = 10)
vak13.grid(row = 9, column = 10)
vak14.grid(row = 11, column = 10)
vak15.grid(row = 13, column = 10)
vak16.grid(row = 15, column = 10)

vak17.grid(row = 31, sticky = 'W')
vak18.grid(row = 33, sticky = 'W')
vak19.grid(row = 35, sticky = 'W')
vak20.grid(row = 37, sticky = 'W')
vak21.grid(row = 39, sticky = 'W')
vak22.grid(row = 41, sticky = 'W')
vak23.grid(row = 43, sticky = 'W')
vak24.grid(row = 45, sticky = 'W')

vak25.grid(row = 31, column = 10)
vak26.grid(row = 33, column = 10)
vak27.grid(row = 35, column = 10)
vak28.grid(row = 37, column = 10)
vak29.grid(row = 39, column = 10)
vak30.grid(row = 41, column = 10)
vak31.grid(row = 43, column = 10)
vak32.grid(row = 45, column = 10)

# entry1.grid(row = 1, column = 1)
# entry2.grid(row = 3, column = 1)
# entry3.grid(row = 5, column = 1)
# entry4.grid(row = 7, column = 1)
# entry5.grid(row = 9, column = 1)
entry6.grid(row = 11, column = 1)
entry7.grid(row = 13, column = 1)
entry8.grid(row = 15, column = 1)

# entry9.grid(row = 1, column = 11)
# entry10.grid(row = 3, column = 11)
# entry11.grid(row = 5, column = 11)
# entry12.grid(row = 7, column = 11)
# entry13.grid(row = 9, column = 11)
entry14.grid(row = 11, column = 11)
entry15.grid(row = 13, column = 11)
entry16.grid(row = 15, column = 11)

# entry17.grid(row = 31, column = 1)
entry18.grid(row = 33, column = 1)
entry19.grid(row = 35, column = 1)
entry20.grid(row = 37, column = 1)
entry21.grid(row = 39, column = 1)
entry22.grid(row = 41, column = 1)
entry23.grid(row = 43, column = 1)
entry24.grid(row = 45, column = 1)

# entry25.grid(row = 31, column = 11)
entry26.grid(row = 33, column = 11)
entry27.grid(row = 35, column = 11)
entry28.grid(row = 37, column = 11)
entry29.grid(row = 39, column = 11)
entry30.grid(row = 41, column = 11)
entry31.grid(row = 43, column = 11)
entry32.grid(row = 45, column = 11)

selectie1.grid(row = 1, column = 2)
selectie2.grid(row = 3, column = 2)
selectie3.grid(row = 5, column = 2)
selectie4.grid(row = 7, column = 2)
selectie5.grid(row = 9, column = 2)
selectie6.grid(row = 11, column = 2)
selectie7.grid(row = 13, column = 2)
selectie8.grid(row = 15, column = 2)

selectie9.grid(row = 1, column = 12)
selectie10.grid(row = 3, column = 12)
selectie11.grid(row = 5, column = 12)
selectie12.grid(row = 7, column = 12)
selectie13.grid(row = 9, column = 12)
selectie14.grid(row = 11, column = 12)
selectie15.grid(row = 13, column = 12)
selectie16.grid(row = 15, column = 12)

selectie17.grid(row = 31, column = 2)
selectie18.grid(row = 33, column = 2)
selectie19.grid(row = 35, column = 2)
selectie20.grid(row = 37, column = 2)
selectie21.grid(row = 39, column = 2)
selectie22.grid(row = 41, column = 2)
selectie23.grid(row = 43, column = 2)
selectie24.grid(row = 45, column = 2)

selectie25.grid(row = 31, column = 12)
selectie26.grid(row = 33, column = 12)
selectie27.grid(row = 35, column = 12)
selectie28.grid(row = 37, column = 12)
selectie29.grid(row = 39, column = 12)
selectie30.grid(row = 41, column = 12)
selectie31.grid(row = 43, column = 12)
selectie32.grid(row = 45, column = 12)

# entry1.bind('<KeyRelease>', functools.partial(on_keyrelease,number=1))
# entry2.bind('<KeyRelease>', functools.partial(on_keyrelease,number=2))
# entry3.bind('<KeyRelease>', functools.partial(on_keyrelease,number=3))
# entry4.bind('<KeyRelease>', functools.partial(on_keyrelease,number=4))
# entry5.bind('<KeyRelease>', functools.partial(on_keyrelease,number=5))
entry6.bind('<KeyRelease>', functools.partial(on_keyrelease,number=6))
entry7.bind('<KeyRelease>', functools.partial(on_keyrelease,number=7))
entry8.bind('<KeyRelease>', functools.partial(on_keyrelease,number=8))

# entry9.bind('<KeyRelease>', functools.partial(on_keyrelease,number=9))
# entry10.bind('<KeyRelease>', functools.partial(on_keyrelease,number=10))
# entry11.bind('<KeyRelease>', functools.partial(on_keyrelease,number=11))
# entry12.bind('<KeyRelease>', functools.partial(on_keyrelease,number=12))
# entry13.bind('<KeyRelease>', functools.partial(on_keyrelease,number=13))
entry14.bind('<KeyRelease>', functools.partial(on_keyrelease,number=14))
entry15.bind('<KeyRelease>', functools.partial(on_keyrelease,number=15))
entry16.bind('<KeyRelease>', functools.partial(on_keyrelease,number=16))

# entry17.bind('<KeyRelease>', functools.partial(on_keyrelease,number=17))
entry18.bind('<KeyRelease>', functools.partial(on_keyrelease,number=18))
entry19.bind('<KeyRelease>', functools.partial(on_keyrelease,number=19))
entry20.bind('<KeyRelease>', functools.partial(on_keyrelease,number=20))
entry21.bind('<KeyRelease>', functools.partial(on_keyrelease,number=21))
entry22.bind('<KeyRelease>', functools.partial(on_keyrelease,number=22))
entry23.bind('<KeyRelease>', functools.partial(on_keyrelease,number=23))
entry24.bind('<KeyRelease>', functools.partial(on_keyrelease,number=24))

# entry25.bind('<KeyRelease>', functools.partial(on_keyrelease,number=25))
entry26.bind('<KeyRelease>', functools.partial(on_keyrelease,number=26))
entry27.bind('<KeyRelease>', functools.partial(on_keyrelease,number=27))
entry28.bind('<KeyRelease>', functools.partial(on_keyrelease,number=28))
entry29.bind('<KeyRelease>', functools.partial(on_keyrelease,number=29))
entry30.bind('<KeyRelease>', functools.partial(on_keyrelease,number=30))
entry31.bind('<KeyRelease>', functools.partial(on_keyrelease,number=31))
entry32.bind('<KeyRelease>', functools.partial(on_keyrelease,number=32))

###
listbox_height = 2

# listbox1 = tk.Listbox(root,height=listbox_height)
# listbox1.grid(row = 2, column = 1)
# listbox1.bind('<<ListboxSelect>>', functools.partial(on_select,number=1, semester=1))
# listbox_update(listbox1,options)
#
# listbox2 = tk.Listbox(root,height=listbox_height)
# listbox2.grid(row = 4, column = 1)
# listbox2.bind('<<ListboxSelect>>', functools.partial(on_select,number=2, semester=1))
# listbox_update(listbox2,options)
#
# listbox3 = tk.Listbox(root,height=listbox_height)
# listbox3.grid(row = 6, column = 1)
# listbox3.bind('<<ListboxSelect>>', functools.partial(on_select,number=3, semester=1))
# listbox_update(listbox3,options)
#
# listbox4 = tk.Listbox(root,height=listbox_height)
# listbox4.grid(row = 8, column = 1)
# listbox4.bind('<<ListboxSelect>>', functools.partial(on_select,number=4, semester=1))
# listbox_update(listbox4,options)
#
# listbox5 = tk.Listbox(root,height=listbox_height)
# listbox5.grid(row = 10, column = 1)
# listbox5.bind('<<ListboxSelect>>', functools.partial(on_select,number=5, semester=1))
# listbox_update(listbox5,options)

listbox6 = tk.Listbox(root,height=listbox_height)
listbox6.grid(row = 12, column = 1)
listbox6.bind('<<ListboxSelect>>', functools.partial(on_select,number=6, semester=1))
listbox_update(listbox6,options)

listbox7 = tk.Listbox(root,height=listbox_height)
listbox7.grid(row = 14, column = 1)
listbox7.bind('<<ListboxSelect>>', functools.partial(on_select,number=7, semester=1))
listbox_update(listbox7,options)

listbox8 = tk.Listbox(root,height=listbox_height)
listbox8.grid(row = 16, column = 1)
listbox8.bind('<<ListboxSelect>>', functools.partial(on_select,number=8, semester=1))
listbox_update(listbox8,options)

# listbox9 = tk.Listbox(root,height=listbox_height)
# listbox9.grid(row = 2, column = 11)
# listbox9.bind('<<ListboxSelect>>', functools.partial(on_select,number=9, semester=2))
# listbox_update(listbox9,options)
#
# listbox10 = tk.Listbox(root,height=listbox_height)
# listbox10.grid(row = 4, column = 11)
# listbox10.bind('<<ListboxSelect>>', functools.partial(on_select,number=10, semester=2))
# listbox_update(listbox10,options)
#
# listbox11 = tk.Listbox(root,height=listbox_height)
# listbox11.grid(row = 6, column = 11)
# listbox11.bind('<<ListboxSelect>>', functools.partial(on_select,number=11, semester=2))
# listbox_update(listbox11,options)
#
# listbox12 = tk.Listbox(root,height=listbox_height)
# listbox12.grid(row = 8, column = 11)
# listbox12.bind('<<ListboxSelect>>', functools.partial(on_select,number=12, semester=2))
# listbox_update(listbox12,options)
#
# listbox13 = tk.Listbox(root,height=listbox_height)
# listbox13.grid(row = 10, column = 11)
# listbox13.bind('<<ListboxSelect>>', functools.partial(on_select,number=13, semester=2))
# listbox_update(listbox13,options)

listbox14 = tk.Listbox(root,height=listbox_height)
listbox14.grid(row = 12, column = 11)
listbox14.bind('<<ListboxSelect>>', functools.partial(on_select,number=14, semester=2))
listbox_update(listbox14,options)

listbox15 = tk.Listbox(root,height=listbox_height)
listbox15.grid(row = 14, column = 11)
listbox15.bind('<<ListboxSelect>>', functools.partial(on_select,number=15, semester=2))
listbox_update(listbox15,options)

listbox16 = tk.Listbox(root,height=listbox_height)
listbox16.grid(row = 16, column = 11)
listbox16.bind('<<ListboxSelect>>', functools.partial(on_select,number=16, semester=2))
listbox_update(listbox16,options)

# listbox17 = tk.Listbox(root,height=listbox_height)
# listbox17.grid(row = 32, column = 1)
# listbox17.bind('<<ListboxSelect>>', functools.partial(on_select,number=17, semester=1))
# listbox_update(listbox17,options)

listbox18 = tk.Listbox(root,height=listbox_height)
listbox18.grid(row = 34, column = 1)
listbox18.bind('<<ListboxSelect>>', functools.partial(on_select,number=18, semester=1))
listbox_update(listbox18,options)

listbox19 = tk.Listbox(root,height=listbox_height)
listbox19.grid(row = 36, column = 1)
listbox19.bind('<<ListboxSelect>>', functools.partial(on_select,number=19, semester=1))
listbox_update(listbox19,options)

listbox20 = tk.Listbox(root,height=listbox_height)
listbox20.grid(row = 38, column = 1)
listbox20.bind('<<ListboxSelect>>', functools.partial(on_select,number=20, semester=1))
listbox_update(listbox20,options)

listbox21 = tk.Listbox(root,height=listbox_height)
listbox21.grid(row = 40, column = 1)
listbox21.bind('<<ListboxSelect>>', functools.partial(on_select,number=21, semester=1))
listbox_update(listbox21,options)

listbox22 = tk.Listbox(root,height=listbox_height)
listbox22.grid(row = 42, column = 1)
listbox22.bind('<<ListboxSelect>>', functools.partial(on_select,number=22, semester=1))
listbox_update(listbox22,options)

listbox23 = tk.Listbox(root,height=listbox_height)
listbox23.grid(row = 44, column = 1)
listbox23.bind('<<ListboxSelect>>', functools.partial(on_select,number=23, semester=1))
listbox_update(listbox23,options)

listbox24 = tk.Listbox(root,height=listbox_height)
listbox24.grid(row = 46, column = 1)
listbox24.bind('<<ListboxSelect>>', functools.partial(on_select,number=24, semester=1))
listbox_update(listbox24,options)

# listbox25 = tk.Listbox(root,height=listbox_height)
# listbox25.grid(row = 32, column = 11)
# listbox25.bind('<<ListboxSelect>>', functools.partial(on_select,number=25, semester=2))
# listbox_update(listbox25,options)

listbox26 = tk.Listbox(root,height=listbox_height)
listbox26.grid(row = 34, column = 11)
listbox26.bind('<<ListboxSelect>>', functools.partial(on_select,number=26, semester=2))
listbox_update(listbox26,options)

listbox27 = tk.Listbox(root,height=listbox_height)
listbox27.grid(row = 36, column = 11)
listbox27.bind('<<ListboxSelect>>', functools.partial(on_select,number=27, semester=2))
listbox_update(listbox27,options)

listbox28 = tk.Listbox(root,height=listbox_height)
listbox28.grid(row = 38, column = 11)
listbox28.bind('<<ListboxSelect>>', functools.partial(on_select,number=28, semester=2))
listbox_update(listbox28,options)

listbox29 = tk.Listbox(root,height=listbox_height)
listbox29.grid(row = 40, column = 11)
listbox29.bind('<<ListboxSelect>>', functools.partial(on_select,number=29, semester=2))
listbox_update(listbox29,options)

listbox30 = tk.Listbox(root,height=listbox_height)
listbox30.grid(row = 42, column = 11)
listbox30.bind('<<ListboxSelect>>', functools.partial(on_select,number=30, semester=2))
listbox_update(listbox30,options)

listbox31 = tk.Listbox(root,height=listbox_height)
listbox31.grid(row = 44, column = 11)
listbox31.bind('<<ListboxSelect>>', functools.partial(on_select,number=31, semester=2))
listbox_update(listbox31,options)

listbox32 = tk.Listbox(root,height=listbox_height)
listbox32.grid(row = 46, column = 11)
listbox32.bind('<<ListboxSelect>>', functools.partial(on_select,number=32, semester=2))
listbox_update(listbox32,options)

###

stp1.grid(row = 1, column = 3)
stp2.grid(row = 3, column = 3)
stp3.grid(row = 5, column = 3)
stp4.grid(row = 7, column = 3)
stp5.grid(row = 9, column = 3)
stp6.grid(row = 11, column = 3)
stp7.grid(row = 13, column = 3)
stp8.grid(row = 15, column = 3)

stp9.grid(row = 1, column = 13)
stp10.grid(row = 3, column = 13)
stp11.grid(row = 5, column = 13)
stp12.grid(row = 7, column = 13)
stp13.grid(row = 9, column = 13)
stp14.grid(row = 11, column = 13)
stp15.grid(row = 13, column = 13)
stp16.grid(row = 15, column = 13)

stp17.grid(row = 31, column = 3)
stp18.grid(row = 33, column = 3)
stp19.grid(row = 35, column = 3)
stp20.grid(row = 37, column = 3)
stp21.grid(row = 39, column = 3)
stp22.grid(row = 41, column = 3)
stp23.grid(row = 43, column = 3)
stp24.grid(row = 45, column = 3)

stp25.grid(row = 31, column = 13)
stp26.grid(row = 33, column = 13)
stp27.grid(row = 35, column = 13)
stp28.grid(row = 37, column = 13)
stp29.grid(row = 39, column = 13)
stp30.grid(row = 41, column = 13)
stp31.grid(row = 43, column = 13)
stp32.grid(row = 45, column = 13)

proj1.grid(row = 1, column = 4)
proj2.grid(row = 3, column = 4)
proj3.grid(row = 5, column = 4)
proj4.grid(row = 7, column = 4)
proj5.grid(row = 9, column = 4)
proj6.grid(row = 11, column = 4)
proj7.grid(row = 13, column = 4)
proj8.grid(row = 15, column = 4)

proj9.grid(row = 1, column = 14)
proj10.grid(row = 3, column = 14)
proj11.grid(row = 5, column = 14)
proj12.grid(row = 7, column = 14)
proj13.grid(row = 9, column = 14)
proj14.grid(row = 11, column = 14)
proj15.grid(row = 13, column = 14)
proj16.grid(row = 15, column = 14)

proj17.grid(row = 31, column = 4)
proj18.grid(row = 33, column = 4)
proj19.grid(row = 35, column = 4)
proj20.grid(row = 37, column = 4)
proj21.grid(row = 39, column = 4)
proj22.grid(row = 41, column = 4)
proj23.grid(row = 43, column = 4)
proj24.grid(row = 45, column = 4)

proj25.grid(row = 31, column = 14)
proj26.grid(row = 33, column = 14)
proj27.grid(row = 35, column = 14)
proj28.grid(row = 37, column = 14)
proj29.grid(row = 39, column = 14)
proj30.grid(row = 41, column = 14)
proj31.grid(row = 43, column = 14)
proj32.grid(row = 45, column = 14)

mond1.grid(row = 1, column = 5)
mond2.grid(row = 3, column = 5)
mond3.grid(row = 5, column = 5)
mond4.grid(row = 7, column = 5)
mond5.grid(row = 9, column = 5)
mond6.grid(row = 11, column = 5)
mond7.grid(row = 13, column = 5)
mond8.grid(row = 15, column = 5)

mond9.grid(row = 1, column = 15)
mond10.grid(row = 3, column = 15)
mond11.grid(row = 5, column = 15)
mond12.grid(row = 7, column = 15)
mond13.grid(row = 9, column = 15)
mond14.grid(row = 11, column = 15)
mond15.grid(row = 13, column = 15)
mond16.grid(row = 15, column = 15)

mond17.grid(row = 31, column = 5)
mond18.grid(row = 33, column = 5)
mond19.grid(row = 35, column = 5)
mond20.grid(row = 37, column = 5)
mond21.grid(row = 39, column = 5)
mond22.grid(row = 41, column = 5)
mond23.grid(row = 43, column = 5)
mond24.grid(row = 45, column = 5)

mond25.grid(row = 31, column = 15)
mond26.grid(row = 33, column = 15)
mond27.grid(row = 35, column = 15)
mond28.grid(row = 37, column = 15)
mond29.grid(row = 39, column = 15)
mond30.grid(row = 41, column = 15)
mond31.grid(row = 43, column = 15)
mond32.grid(row = 45, column = 15)

update()

root.mainloop()