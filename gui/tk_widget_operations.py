def modify_contents_of_disabled_text_widget(modify_text_widget_fun):
    def text_widget_wrapper(*args):
        text_widget = args[0]
        was_active = was_widget_active(text_widget)
        if was_active  != "normal":
            activate_widgets_before_making_changes(text_widget)

        modify_text_widget_fun(*args)

        if was_active != "normal":
            deactivate_widgets(text_widget)
    return text_widget_wrapper


@modify_contents_of_disabled_text_widget
def clear_text_widget(pa_text_widget):
    pa_text_widget.delete("1.0", "end")


@modify_contents_of_disabled_text_widget
def fill_text_widget(pa_text_widget, pa_items):
    add_entries_into_textbox(pa_text_widget, pa_items)


def add_entries_into_textbox(pa_text_widget, pa_items):
    for item in pa_items:
        item += "\n"
        pa_text_widget.insert("end", item)


def clear_text_widgets(*pa_widgets):
    for widget in pa_widgets:
        clear_text_widget(widget)


def was_widget_active(pa_widget):
    return pa_widget.cget("state")


def activate_widgets_before_making_changes(*pa_widgets):
    for widget in pa_widgets:
        widget.configure(state="normal")


def deactivate_widgets(*pa_widgets):
    for widget in pa_widgets:
        widget.configure(state="disabled")

