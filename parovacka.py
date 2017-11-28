from tkinter import *
from random import shuffle


def sparuj():
    # Vytvor unikatne dvojice
    zoznamUcastnikovStr = zoznamUcastnikov.get("1.0", "end-1c")
    zoznamUcastnikovPrvych = zoznamUcastnikovStr.split()
    zoznamUcastnikovDruhych = list(zoznamUcastnikovPrvych)

    uzMamUnikatneDvojce = False
    uzMamDvojiceBezReciprocity = False

    while uzMamUnikatneDvojce == False:
        shuffle(zoznamUcastnikovDruhych)

        uzMamUnikatneDvojce = suDvojiceUnikatne(
            zoznamUcastnikovPrvych,
            zoznamUcastnikovDruhych)

        uzMamDvojiceBezReciprocity = suDvojiceBezReciprocity(
            zoznamUcastnikovPrvych,
            zoznamUcastnikovDruhych)

        print()
        break

def suDvojiceUnikatne(zoznamUcastnikov, zoznamDvojiciek):
    # print(zoznamUcastnikov)
    # print(zoznamDvojiciek)

    for i in range(len(zoznamUcastnikov)):
        prvy = zoznamUcastnikov[i]
        druhy = zoznamDvojiciek[i]
        # print(prvy + ":" + druhy)

        if prvy == druhy:
            # print("Nemozem dat darcek sam sebe!")
            return False

    # print("Kazdy da niekomu darcek")
    return True

# TODO - urobit reciprocity checkbox do GUI
def suDvojiceBezReciprocity(zoznamUcastnikov, zoznamDvojiciek):
    for i in range(len(zoznamUcastnikov)):
        prvaDvojica = vytvorDvojicu(
            zoznamUcastnikov[i],
            zoznamDvojiciek[i])

        for j in range(len(zoznamDvojiciek)):
            if i != j:
                inaDvojica = vytvorDvojicu(
                    zoznamUcastnikov[j],
                    zoznamDvojiciek[j])

                nakolkoSuDvojiceZhodne = kolkoPrvkovObochDvojicJeZhodnych(
                    prvaDvojica,
                    inaDvojica)
                if nakolkoSuDvojiceZhodne == 2:
                    # print(dvojiceSuZhodne)
                    return False

    return True

def vytvorDvojicu(prvy, druhy):
    return set([prvy, druhy])

def kolkoPrvkovObochDvojicJeZhodnych(prvaDvojica, inaDvojica):
    return len(prvaDvojica.intersection(inaDvojica))


root = Tk()
root.title("Párovačka")
root.geometry("500x300")
root.grid()

buttonSparuj = Button(root, text="Spáruj", width = 80, height=50, anchor="center", command=sparuj)
buttonSparuj.grid(row=0, column=0, sticky='NSEW')

zoznamUcastnikov = Text(root, width = 100, height=100)
zoznamUcastnikov.grid(column=1, row=0, sticky='NSEW')

sKymBudeVoDvojici = Text(root, width = 120, height=100)
sKymBudeVoDvojici.grid(column=2, row=0, sticky='NSEW')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.mainloop()

# Zdroje:
# https://stackoverflow.com/questions/42560585/how-do-i-center-text-in-the-tkinter-text-widget
# https://stackoverflow.com/a/30908374 => Python Tkinter - resize widgets evenly in a window
# https://www.tutorialspoint.com/python/tk_listbox.htm => pocet poloziek v Listboxe
# https://www.youtube.com/watch?v=FueIPFqRyyY => Ulozit obsah Text widgetu do premennej
# https://stackoverflow.com/questions/743806/how-to-split-a-string-into-a-list
# https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
# https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
# http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/ => how to make for loop with index
