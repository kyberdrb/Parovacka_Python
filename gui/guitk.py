from tkinter import Tk, Text, Button
import gui.tk_widget_operations as tk_ops
from assignment import assignment


class GuiTk:
    def __init__(self, pa_root_window):
        self.master = pa_root_window
        self.set_up_window()
        self.add_widgets()
        self.assignments = None

    def set_up_window(self):
        self.master.title("Párovačka")

        # TODO - calculate window dimensions according to the screen resolution
        self.master.geometry("500x300")
        self.master.grid()

    def add_widgets(self):
        self.button_make_couples = Button(
            self.master,
            text="Spáruj",
            width=80,
            height=50,
            anchor="center",
            command=self.make_couples
        )
        self.button_make_couples.grid(row=0, column=0, sticky="NSEW")

        self.tw_participants = Text(self.master, width=100, height=100)
        self.tw_participants.grid(column=1, row=0, sticky="NSEW")

        self.tw_couples = Text(self.master, width=120, height=100)
        tk_ops.deactivate_widgets(self.tw_couples)
        self.tw_couples.grid(column=2, row=0, sticky="NSEW")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    def make_couples(self):
        tk_ops.clear_text_widget(self.tw_couples)
        self.assignments = assignment.Assignments(self.retrieve_list_of_participants())
        tk_ops.clear_text_widget(self.tw_participants)
        tk_ops.fill_text_box(self.tw_participants, self.assignments.gifters)
        self.assignments.create_list_of_gift_takers()
        self.display_couples()

    def retrieve_list_of_participants(self):
        participants = self.tw_participants.get("1.0", "end-1c")
        participants_names = participants.split()
        return participants_names

    def display_couples(self):
        tk_ops.fill_text_box(self.tw_couples, self.assignments.giftees)


if __name__ == "__main__":
    root_window = Tk()
    GuiTk(root_window)
    root_window.mainloop()
