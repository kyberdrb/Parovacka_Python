import tkinter
from random import shuffle

class GUI(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        buttonSparuj = tkinter.Button(self,
                                      text="Spáruj",
                                      width=80,
                                      height=50,
                                      anchor="center",
                                      command=self.sparuj)

        buttonSparuj.grid(row=0, column=0, sticky='NSEW')

        zoznamUcastnikov = tkinter.Text(self, width=100, height=100)
        zoznamUcastnikov.grid(column=1, row=0, sticky='NSEW')

        sKymBudeVoDvojici = tkinter.Text(self, width=120, height=100)
        sKymBudeVoDvojici.grid(column=2, row=0, sticky='NSEW')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def sparuj(self):
        # Vytvor unikatne dvojice
        zoznamUcastnikovStr = self.zoznamUcastnikov.get("1.0", "end-1c")
        zoznamUcastnikovPrvych = zoznamUcastnikovStr.split()
        zoznamUcastnikovDruhych = list(zoznamUcastnikovPrvych)

        uzMamUnikatneDvojce = False
        uzMamDvojiceBezReciprocity = False

        while uzMamUnikatneDvojce == False:
            shuffle(zoznamUcastnikovDruhych)

            uzMamUnikatneDvojce = self.suDvojiceUnikatne(
                zoznamUcastnikovPrvych,
                zoznamUcastnikovDruhych)

            uzMamDvojiceBezReciprocity = self.suDvojiceBezReciprocity(
                zoznamUcastnikovPrvych,
                zoznamUcastnikovDruhych)

            print()
            break

    def suDvojiceUnikatne(self, zoznamUcastnikov, zoznamDvojiciek):
        print(zoznamUcastnikov)
        print(zoznamDvojiciek)

        for i in range(len(zoznamUcastnikov)):
            prvy = zoznamUcastnikov[i]
            druhy = zoznamDvojiciek[i]
            print(prvy + ":" + druhy)
            if prvy == druhy:
                print("Nemozem dat darcek sam sebe!")
                return False

        print("Kazdy da niekomu darcek")
        return True

    # TODO - urobit reciprocity checkbox do GUI
    def suDvojiceBezReciprocity(self, zoznamUcastnikov, zoznamDvojiciek):
        for i in range(len(zoznamUcastnikov)):
            prvy = zoznamUcastnikov[i]
            druhy = zoznamDvojiciek[i]
            prva_dvojica = set([prvy, druhy])

            for j in range(len(zoznamDvojiciek)):
                if i != j:
                    iny_prvy = zoznamUcastnikov[j]
                    iny_druhy = zoznamDvojiciek[j]
                    ina_dvojica = set([iny_prvy, iny_druhy])
                    prienik = prva_dvojica.intersection(ina_dvojica)
                    if prienik is not "":
                        print(prienik)
                        return False

        return True


if __name__ == "__main__":
    app = GUI(None)
    app.title("Párovačka")
    app.geometry("500x300")
    app.mainloop()
