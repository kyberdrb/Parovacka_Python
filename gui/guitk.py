from tkinter import Tk, Text, Button
import gui.tk_widget_operations as tk_ops
from assignment import assignment


class GuiTk:
    def __init__(self, pa_root_window, pa_window_width, pa_window_height):
        self.master = pa_root_window
        self.window_width = pa_window_width
        self.window_height = pa_window_height
        self.set_up_window()
        self.add_widgets()
        self.assignments = None

    def set_up_window(self):
        self.master.title("Párovačka")
        window_dimensions = (str(round(self.window_width))) + \
                            "x" + \
                            (str(round(self.window_height)))
        self.master.geometry(window_dimensions)
        self.master.grid()

    # TODO maybe add resizing functionality to all widgets? panedwindow - sash
    def add_widgets(self):
        self.button_make_couples = Button(self.master, text="Spáruj", width=10, command=self.make_couples)
        self.button_make_couples.grid(row=0, column=0, sticky="NSEW")

        self.tw_participants = Text(self.master, width=60)
        self.tw_participants.grid(row=0, column=1, sticky="NSEW")

        self.tw_couples = Text(self.master, state='disabled')
        self.tw_couples.grid(row=0, column=2, sticky="NSEW")

        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    def make_couples(self):
        tk_ops.clear_text_widget(self.tw_couples)
        self.assignments = assignment.Assignments(self.retrieve_list_of_participants())
        tk_ops.clear_text_widget(self.tw_participants)
        tk_ops.fill_text_box(self.tw_participants, self.assignments.gifters)
        self.assignments.create_list_of_giftees()
        self.display_couples()

    def retrieve_list_of_participants(self):
        participants = self.tw_participants.get("1.0", "end-1c")
        participants_names = participants.split()
        return participants_names

    def display_couples(self):
        tk_ops.fill_text_box(self.tw_couples, self.assignments.giftees)


if __name__ == "__main__":
    root_window = Tk()
    window_width = root_window .winfo_screenwidth() / 2
    window_height = root_window .winfo_screenheight() / 2
    GuiTk(root_window, window_width, window_height)
    root_window.mainloop()
