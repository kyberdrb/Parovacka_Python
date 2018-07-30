from tkinter import Tk, Text, Button


class GuiTk:
    def __init__(self, pa_root_window):
        self.master = pa_root_window
        pa_root_window.title("Párovačka")

        pa_root_window.geometry("500x300")
        pa_root_window.grid()

        button_sparuj = Button(
            pa_root_window,
            text="Spáruj",
            width=80,
            height=50,
            anchor="center",
            command=self.make_couples
        )
        button_sparuj.grid(row=0, column=0, sticky='NSEW')

        zoznam_ucastnikov = Text(pa_root_window, width=100, height=100)
        zoznam_ucastnikov.grid(column=1, row=0, sticky='NSEW')

        s_kym_bude_vo_dvojici = Text(pa_root_window, width=120, height=100)
        s_kym_bude_vo_dvojici.config(state="disabled")

        # Before and after inserting, change the state, otherwise it won't update
        s_kym_bude_vo_dvojici.insert('end', 'Disabled Some Text')
        s_kym_bude_vo_dvojici.configure(state='normal')
        s_kym_bude_vo_dvojici.insert('end', 'Some Text')
        s_kym_bude_vo_dvojici.configure(state='disabled')

        s_kym_bude_vo_dvojici.grid(column=2, row=0, sticky='NSEW')

        pa_root_window.grid_columnconfigure(0, weight=1)
        pa_root_window.grid_columnconfigure(1, weight=1)
        pa_root_window.grid_columnconfigure(2, weight=1)
        pa_root_window.grid_rowconfigure(0, weight=1)

    def make_couples(self):
        print("Greetings!")


if __name__ == "__main__":
    root_window = Tk()
    my_gui = GuiTk(root_window)
    root_window.mainloop()
