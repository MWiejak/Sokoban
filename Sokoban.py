from turtle import *
from time import sleep
import tkinter as TK

# ----- Stałe ------------
magazynier = 'M'
skrzynia   = '*'
ściana     = '#'
cel        = '!'
wolne      = '.'
dziura     = 'D'
nic        = ' '
#-----Funkcje pomocnicze_______________________________________________________
def tło():
    marg_x = 4
    marg_y = 9

    min_x = -window_width()//2 + marg_x
    min_y = -window_height()//2 + marg_y
    max_x = window_width() // 2 - 10
    max_y = window_height() // 2 - 3
    return min_x,min_y,max_y,marg_x,marg_y

def prostokąt(x,y):
    fd(x)
    rt(90)
    fd(y)
    rt(90)
    fd(x)
    rt(90)
    fd(y)
    rt(90)

def moje_goto(x,y):
    up()
    goto(x,y)
    down()

def hop(x,y):
    up()
    fd(x)
    lt(90)
    fd(y)
    rt(90)
    down()



#-------------------------Funkcje używane przy rysowaniu-----------------------------------------------
def ramka(min_x,min_y,max_y,marg_x,marg_y):
    color("DarkRed")
    moje_goto(min_x,max_y)
    pensize(4)
    goto(-min_x-marg_y,max_y)
    goto(-min_x-marg_y,min_y+marg_x)
    goto(min_x,min_y+marg_x)
    goto(min_x,max_y)
    color("Black")

def pole_informacyjne(min_x,min_y,max_y,marg_x,marg_y):
    moje_goto(min_x,max_y)
    bok1=((-min_x-marg_y)-min_x) #bok1 i bok2 to wymiary okna z uwzględnieniem ramki.
    bok2=(max_y-(min_y+marg_x))
    pensize(4)
    color("DarkRed")
    fillcolor("Green")
    begin_fill()
    prostokąt(bok1,bok2/13)
    end_fill()
    color("Black")
    hop(0,-bok2/13)
    return bok1,bok2

def rysuj_magazyniera(bok_x,bok_y):
    if bok_x>=bok_y:
        hop(bok_x/2,-bok_y)
        fillcolor("Orange")
        begin_fill()
        circle(bok_y/2)
        end_fill()
        hop(-bok_x/2,bok_y)
    else:
        hop(bok_x/2,-(bok_y+bok_x)/2)
        fillcolor("Orange")
        begin_fill()
        circle(bok_x/2)
        end_fill()
        hop(-bok_x/2,(bok_y+bok_x)/2)

def rysuj_skrzynię(bok_x,bok_y):
    hop(bok_x/4,-bok_y/4)
    fillcolor("Brown")
    begin_fill()
    prostokąt(bok_x/2,bok_y/2)
    end_fill()
    hop(-bok_x/4,bok_y/4)

def rysuj_puste(bok_x,bok_y):
    fillcolor("LightBlue")
    begin_fill()
    prostokąt(bok_x,bok_y)
    end_fill()

def rysuj_dziurę(bok_x,bok_y):
    fillcolor("Red")
    begin_fill()
    prostokąt(bok_x,bok_y)
    end_fill()

def rysuj_cel(bok_x,bok_y):
    fillcolor("Gold")
    begin_fill()
    prostokąt(bok_x,bok_y)
    end_fill()

def rysuj_ścianę(bok_x,bok_y):
    fillcolor("Black")
    begin_fill()
    prostokąt(bok_x,bok_y)
    end_fill()

def rysuj_puste_pola(ile_wierszy,ile_kolumn,lista_wierszy,bok_x,bok_y):
    pensize(2)
    while i<ile_kolumn:
        a=0
        while a<ile_wierszy:
            wypełnij_pole(bok_x,bok_y,lista_wierszy,a,i)
            hop(0,-bok_y)
            a+=1
        moje_goto(min_x,c)
        hop((i+1)*bok_x,0)
        i+=1
        pass



#-------------------------PLansza: wczytywanie, reprezentacja i rysowanie------------------------------
def plansza(projekt_planszy):
    lista_wierszy=[]
    linia=[]
    with open(projekt_planszy, "r", encoding="utf-8") as plik:
        for wiersz in plik:
            wiersz=wiersz.strip("\n")
            for znak in wiersz:
                if znak==magazynier:
                    pole=[wolne,magazynier]
                elif znak==skrzynia:
                    pole=[wolne,skrzynia]
                else:
                    pole=[znak,nic]
                linia.append(pole)
            lista_wierszy.append(linia)
            linia=[]
        ile_wierszy=len(lista_wierszy)
        ile_kolumn=len(lista_wierszy[0])
        return ile_wierszy,ile_kolumn, lista_wierszy

def wypełnij_pole(bok_x,bok_y,lista_wierszy,a,i):
    for b in range(2):
        if lista_wierszy[a][i][b]==wolne:
            rysuj_puste(bok_x,bok_y)
        elif lista_wierszy[a][i][b]==ściana:
            rysuj_ścianę(bok_x,bok_y)
        elif lista_wierszy[a][i][b]==dziura:
            rysuj_dziurę(bok_x,bok_y)
        elif lista_wierszy[a][i][b]==cel:
            rysuj_cel(bok_x,bok_y)
        elif lista_wierszy[a][i][b]==skrzynia:
            rysuj_skrzynię(bok_x,bok_y)
        elif lista_wierszy[a][i][b]==magazynier:
            rysuj_magazyniera(bok_x,bok_y)


def rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy):
    min_x,min_y ,max_y,marg_x,marg_y=tło()
    bok1,bok2=pole_informacyjne(min_x,min_y ,max_y,marg_x,marg_y)
    start=pos()
    bok2=12*bok2/13 # nowy rozmiar boku 2 po uwzględnieniu pola informayjnego
    bok_x=bok1/ile_kolumn # bok_x i bok_y to rozmiar pojedynczego pola na planszy
    bok_y=bok2/ile_wierszy
    pensize(2)
    i =0
    c=ycor() # pionowa współrzędna początkowego położenia żółwia, do której wraca po każdej iteracji wewnętrznej funkcji while
    while i<ile_kolumn:
        a=0
        while a<ile_wierszy:
            wypełnij_pole(bok_x,bok_y,lista_wierszy,a,i)
            hop(0,-bok_y)
            a+=1
        moje_goto(min_x,c)
        hop((i+1)*bok_x,0)
        i+=1
    ramka(min_x,min_y,max_y,marg_x,marg_y)
    moje_goto(start[0],start[1])

    return bok_x,bok_y,bok2,bok1
#---------------------------------------------------- Rozgrywka: informacje o ruchach i pozycji, oraz funkcja rejestrująca zmiany położenia magzayneira

def szukaj_magazyniera(lista_wierszy,bok_x,bok_y): # funkcja służąca do przesuwania żółwia na magazyniera, oraz do rysowania planszy, po wykodaniu ruchu
    licznik_x=0
    licznik_y=0
    for wiersz in lista_wierszy:
        for pozycja in wiersz:
            if not pozycja[1]==magazynier:
                licznik_x+=1
            else:
                hop(licznik_x*bok_x,-licznik_y*bok_y)
                if bok_x>=bok_y:
                    hop(bok_x/2,-bok_y/2)
                else:
                    hop(bok_x/2,-(bok_y+bok_x)/4)

                return licznik_x,licznik_y
        licznik_x=0
        licznik_y+=1

def informacje(bok2,bok1,licznik_x,licznik_y,liczba_ruchów): # funkcja wyświetlająca liczbę wykonanych ruchów i pozycję magazyniera
    min_x,min_y,max_y,marg_x,marg_y=tło()
    color("Yellow")
    moje_goto(min_x,max_y)
    hop(bok1/4,-13*bok2/(12*26))
    write("Liczba ruchów:        ", align="center", font=("Arial", 20, "normal"))
    hop(bok1/10,0)
    write( liczba_ruchów,align="center",font=("Arial",20,"normal"))
    hop((bok1)/4,0)
    write("Pozycja: ",align="center",font=("Arial",20,"normal"))
    hop(bok1/12,0)
    write((licznik_x,licznik_y),align="center",font=("Arial",20,"normal"))
    moje_goto(-356,283.31)
    color("Orange")

def sprawdź_przegraną(lista_wierszy): #sprawdza również wygraną
    wynik=None
    for wiersz in lista_wierszy:
        for pozycja in wiersz:
            if pozycja==[dziura,skrzynia]:
                wynik=False
    licznik_skrzyń=0
    licznik_sukcesów=0
    for wiersz in lista_wierszy:
        for pozycja in wiersz:
            if pozycja[1]==skrzynia:
                licznik_skrzyń+=1
            if pozycja==[cel,skrzynia]:
                licznik_sukcesów+=1
    if licznik_skrzyń==licznik_sukcesów:
        wynik=True
    return wynik





# ------------- Obsługa klawiatury - początek-------------

zdarzenie_klawiatury = ""

def ustaw_kierunek(zd):
    def result():
        global zdarzenie_klawiatury
        zdarzenie_klawiatury = zd
        #print("ustawiam zdarzenie: " + zd)
    return result

def daj_zdarzenie():
    global zdarzenie_klawiatury
    while zdarzenie_klawiatury == "":
        TK._default_root.update()
        sleep(0.01)
    pom = zdarzenie_klawiatury
    zdarzenie_klawiatury = ""
    return pom

def ini_klawiatura():
    for kierunek in ["Up", "Left", "Right", "Down", "k"]:
        onkey(ustaw_kierunek(kierunek.lower()), kierunek)

    listen()

# ------------- Obsługa klawiatury - koniec-------------

def wędruj(lista_wierszy,bok_x,bok_y,ile_wierszy,ile_kolumn,bok2,bok1): #schemat poruszania się, jest w każdym ruchu taki sam
    wędrówka = True
    color("Orange")
    up()
    update()
    liczba_ruchów=0
    while wędrówka:

        zdarzenie = daj_zdarzenie()

        if zdarzenie == "left":    # lewo
            licznik_x,licznik_y=szukaj_magazyniera(lista_wierszy,bok_x,bok_y) #odnajduje pozycję magazyniera
            if not licznik_x==0 and not lista_wierszy[licznik_y][licznik_x-1][1]==skrzynia and not lista_wierszy[licznik_y][licznik_x-1][0]==ściana : #sprawdza, czy ruch może zostać wykonany zgodnie z zasadami gry, jeśli nie przesuwa skrzyni
                lista_wierszy[licznik_y][licznik_x-1][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y][licznik_x-1][1] # zamieniam miejscami drugą pozycję z listy reprezentującej pojednycze pole między odpowiendimi elementami w liście reprezentującej planszę( tu: między kolumną poprzednią względem pozycji magazyniera, w wierszu, w którym znajduje się magazynier)
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy) # rysuje planszę z uwzględnieniem wykonanego ruchu.
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x-1,licznik_y,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)

            elif lista_wierszy[licznik_y][licznik_x-1][1]==skrzynia and not licznik_x-2==-1 and not lista_wierszy[licznik_y][licznik_x-2][1]==skrzynia and not lista_wierszy[licznik_y][licznik_x-2][0]==ściana: # sprawdza czy ruch może zostać wykonany zgodnie z zasadami gry, jeśli przesuwa skrzynię
                lista_wierszy[licznik_y][licznik_x-2][1],lista_wierszy[licznik_y][licznik_x-1][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y][licznik_x-1][1],lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y][licznik_x-2][1] # ta sama operacja, co w przypadku nie przesuwania skrzyni, tylko w obrębie 3 elemntów listy repreentującej planszę.
                rysuj_planszę(ile_wierszy, ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x-1,licznik_y,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
                wynik=sprawdź_przegraną(lista_wierszy)
                if wynik==False:
                    moje_goto(0,0)
                    color("Red")
                    return write("Przegrana :(", align="center", font=("Arial",40,"normal")),color("Orange")
                elif wynik==True:
                    moje_goto(0,0)
                    color("DarkGreen")
                    return write("Wygrana!",align="center",font=("Arial",40,"normal")),color("Orange")
            else:
                continue#<------zapobiega przeskokom kursora wynikłym z zadziałania szukaj_magazyniera
            update()
        elif zdarzenie == "up":  # góra
            licznik_x,licznik_y=szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
            if not licznik_y==0 and not lista_wierszy[licznik_y-1][licznik_x][1]==skrzynia and not lista_wierszy[licznik_y-1][licznik_x][0]==ściana:
                lista_wierszy[licznik_y-1][licznik_x][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y-1][licznik_x][1]
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x,licznik_y-1,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
            elif lista_wierszy[licznik_y-1][licznik_x][1]==skrzynia and not licznik_y-2==-1 and not lista_wierszy[licznik_y-2][licznik_x][1]==skrzynia and not lista_wierszy[licznik_y-2][licznik_x][0]==ściana:
                lista_wierszy[licznik_y-2][licznik_x][1],lista_wierszy[licznik_y-1][licznik_x][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y-1][licznik_x][1],lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y-2][licznik_x][1]
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x,licznik_y-1,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
                wynik=sprawdź_przegraną(lista_wierszy)
                if wynik==False:
                    moje_goto(0,0)
                    color("Red")
                    return write("Przegrana :(", align="center", font=("Arial",40,"normal")),color("Orange")
                elif wynik==True:
                    moje_goto(0,0)
                    color("DarkGreen")
                    return write("Wygrana!",align="center",font=("Arial",40,"normal")),color("Orange")
            else:
                continue
            update()
        elif zdarzenie == "right":  # prawo
            licznik_x,licznik_y=szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
            if not  licznik_x==len(lista_wierszy[0])-1 and not lista_wierszy[licznik_y][licznik_x+1][0]==ściana and not lista_wierszy[licznik_y][licznik_x+1][1]==skrzynia:
                lista_wierszy[licznik_y][licznik_x+1][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y][licznik_x+1][1]
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x+1,licznik_y,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
                #print(lista_wierszy)
            elif not licznik_x==len(lista_wierszy[0])-1 and lista_wierszy[licznik_y][licznik_x+1][1]==skrzynia and not licznik_x+2==len(lista_wierszy[0]) and not lista_wierszy[licznik_y][licznik_x+2][1]==skrzynia and not lista_wierszy[licznik_y][licznik_x+2][0]==ściana:
                lista_wierszy[licznik_y][licznik_x+2][1],lista_wierszy[licznik_y][licznik_x+1][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y][licznik_x+1][1],lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y][licznik_x+2][1]
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x+1,licznik_y,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
                wynik=sprawdź_przegraną(lista_wierszy)
                if wynik==False:
                    moje_goto(0,0)
                    color("Red")
                    return write("Przegrana :(", align="center", font=("Arial",40,"normal")),color("Orange")
                elif wynik==True:
                    moje_goto(0,0)
                    color("DarkGreen")
                    return write("Wygrana!",align="center",font=("Arial",40,"normal")),color("Orange")
            else:
                continue
            update()
        elif zdarzenie == "down":  # dół
            licznik_x,licznik_y=szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
            if not licznik_y==len(lista_wierszy)-1 and not lista_wierszy[licznik_y+1][licznik_x][1]==skrzynia and not lista_wierszy[licznik_y+1][licznik_x][0]==ściana:
                lista_wierszy[licznik_y][licznik_x][1],lista_wierszy[licznik_y+1][licznik_x][1]=lista_wierszy[licznik_y+1][licznik_x][1],lista_wierszy[licznik_y][licznik_x][1]
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x,licznik_y+1,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
            elif not licznik_y==len(lista_wierszy)-1 and lista_wierszy[licznik_y+1][licznik_x][1]==skrzynia and not licznik_y+2==len(lista_wierszy) and not lista_wierszy[licznik_y+2][licznik_x][1]==skrzynia and not lista_wierszy[licznik_y+2][licznik_x][0]==ściana:
                lista_wierszy[licznik_y+2][licznik_x][1],lista_wierszy[licznik_y+1][licznik_x][1],lista_wierszy[licznik_y][licznik_x][1]=lista_wierszy[licznik_y+1][licznik_x][1],lista_wierszy[licznik_y][licznik_x][1], lista_wierszy[licznik_y+2][licznik_x][1]
                rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
                liczba_ruchów+=1
                informacje(bok2,bok1,licznik_x,licznik_y+1,liczba_ruchów)
                szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
                wynik=sprawdź_przegraną(lista_wierszy)
                if wynik==False:
                    moje_goto(0,0)
                    color("Red")
                    return write("Przegrana :(", align="center", font=("Arial",40,"normal")),color("Orange")
                elif wynik==True:
                    moje_goto(0,0)
                    color("DarkGreen")
                    return write("Wygrana!",align="center",font=("Arial",40,"normal")),color("Orange")

            else:
                continue
            update()
        elif zdarzenie == "k":   # koniec
            wędrówka = False
        else:
            print("Nieobsługiwane zdarzenie: " + zdarzenie)
    return lista_wierszy

#--------------------------------------Fumkcja główna
def main(projekt_planszy):
    tracer(0,0)
    ile_wierszy, ile_kolumn,lista_wierszy=plansza(projekt_planszy)
    bok_x,bok_y,bok2,bok1=rysuj_planszę(ile_wierszy,ile_kolumn,lista_wierszy)
    szukaj_magazyniera(lista_wierszy,bok_x,bok_y)
    ini_klawiatura()
    wędruj(lista_wierszy,bok_x,bok_y,ile_wierszy,ile_kolumn,bok2,bok1)
    done()
main("plansza1.txt")
