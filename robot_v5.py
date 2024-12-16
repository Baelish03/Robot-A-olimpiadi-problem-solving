print('Il programma prevede un file di istruzioni, uno di input e uno di output, importanti per l\'esecuzione del programma.')

from os import chdir as cd
import pandas as pd

def a():
    global x,y,d_marker,listax,listay,listamarker
    if d_marker=='N' or d_marker=='n':
        new_marker='w'
        d_marker=new_marker
    elif d_marker=='W' or d_marker=='w':
        new_marker='s'
        d_marker=new_marker
    elif d_marker=='S' or d_marker=='s':
        new_marker='e'
        d_marker=new_marker
    elif d_marker=='E' or d_marker=='e':
        new_marker='n'
        d_marker=new_marker
    listax.append(x)
    listay.append(y)
    listamarker.append(d_marker)
    return x,y,d_marker,listax,listay,listamarker
    
def o():
    global x,y,d_marker,listax,listay,listamarker
    if d_marker=='N' or d_marker=='n':
        new_marker='e'
        d_marker=new_marker
    elif d_marker=='W' or d_marker=='w':
        new_marker='n'
        d_marker=new_marker
    elif d_marker=='S' or d_marker=='s':
        new_marker='w'
        d_marker=new_marker
    elif d_marker=='E' or d_marker=='e':
        new_marker='s'
        d_marker=new_marker
    listax.append(x)
    listay.append(y)
    listamarker.append(d_marker)
    return x,y,d_marker,listax,listay,listamarker

def f(numero_di_passi):
    global x,y,d_marker,listax,listay,listamarker
    if d_marker=='N' or d_marker=='n':
        y=y+numero_di_passi
    elif d_marker=='W' or d_marker=='w':
        x=x-numero_di_passi
    elif d_marker=='S' or d_marker=='s':
        y=y-numero_di_passi
    elif d_marker=='E' or d_marker=='e':
        x=x+numero_di_passi
    listax.append(x)
    listay.append(y)
    listamarker.append(d_marker)
    return x,y,d_marker,listax,listay,listamarker

#output 
def risultato():
    global x,y,d_marker,listax,listay,listamarker,listaicu

    with pd.option_context('display.max_rows',None,'display.max_columns',None,'display.expand_frame_repr',False):
        df=pd.DataFrame()
        df['Comando']=listaicu
        df['X']=pd.Series(listax)
        df['Y']=pd.Series(listay)
        df['Direzione']=pd.Series(listamarker)
        print(df)
        esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')

    p_finale=str([x,y,d_marker])
    p_finale=p_finale.replace(' ','')
    p_finale=p_finale.replace('\'','')

    #output file esterno
    try:
        cd('C:\\Users\\user\\Desktop\\robot_v5')
    except FileNotFoundError:
        cd(path)   

    try:
        with open('output robot v5.txt', 'w') as file:
            out=file.write('Punto di arrivo: ')
            out=file.write(p_finale)
    except FileNotFoundError:
        print('Il file di output non esiste. Ricontrollare il nome del file.')
        esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
        exit()


#input
try:
    cd('C:\\Users\\user\\Desktop\\robot_v5')
except FileNotFoundError:
    try:
        print('Il percorso del file di input non esiste, prova a inserirlo manualmente.')
        path=input('Percorso del file di input: ')
        cd(path)
    except FileNotFoundError:
        print('Il percorso inserito non è corretto.')
        esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
        exit()    

try:
    with open('input robot v5.txt', 'r') as file:
        inp=file.readlines()
except FileNotFoundError:
    print('Il file di input non esiste. Ricontrollare il percorso o il nome del file.')
    esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()

try:
    posizione_inizio=inp[0]
    direzione_inizio=inp[1]
    lista_comandi=inp[2]
except IndexError:
    print('L\'input non è completo. Controllare che siano su righe differnti seguendo le istruzioni')
    esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()


#pulizia input
def pul(inp):
    inp=inp.replace('(','')
    inp=inp.replace(')','')
    inp=inp.replace('[','')
    inp=inp.replace(']','')
    inp=inp.replace('.','')
    inp=inp.replace(';','')
    inp=inp.split(',')
    return inp


#posizione_inizio=pi    direzione_inizio=di    lista_comandi=lc
#gestione input coordinate
pi=posizione_inizio.replace('\n','')
pi=pul(pi)
try:
    x=int(pi[0])
    y=int(pi[1])
except ValueError:
    print('Le coordinate di partenza sono sbagliate')
    esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()

#gestione input direzione
di=direzione_inizio.replace('\n','')
di=pul(di)
di=di[0]
if di!='W' and di!='w' and di!='N' and di!='n'and di!='E' and di!='e'and di!='S' and di!='s':
    print('La direzione di partenza è sbagliata')
    esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()
else:
    d_marker=di

#gestione input lista comandi
lc=lista_comandi.replace('\n','')
lc=pul(lc)
if len(lc)==1:
    print('La lista dei comandi è vuota.')
    esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()

#esecuzione
listaicu=['punto iniziale']
listax=[x]
listay=[y]
listamarker=[d_marker]

for icu in lc:
    listaicu.append(icu)
    if icu=='a':
        a()
    elif icu=='o':
        o()
    elif icu[0]=='f':
        try:
            numero_di_passi=int(icu[1:])
        except ValueError:
            numero_di_passi=1
        f(numero_di_passi)

risultato()

#sviluppato da Emanuele Urso 7-8/7/2020
#input esterno 23/10/2020
#v5 24/02/2023
