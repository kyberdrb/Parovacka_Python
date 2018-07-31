def fill_text_box(pa_text_widget, pa_items):
    activate_widgets_before_making_changes(pa_text_widget)
    for item in pa_items:
        item += "\n"
        pa_text_widget.insert("end", item)

def clear_text_widgets(*pa_widgets):
    for widget in pa_widgets:
        clear_text_widget(widget)


def clear_disabled_text_widgets(clear_text_widget_fun):
    def text_widget_wrapper(pa_text_widget):
        if was_widget_active(pa_text_widget) != "normal":
            activate_widgets_before_making_changes(pa_text_widget)
            clear_text_widget_fun(pa_text_widget)
            deactivate_widgets(pa_text_widget)
        else:
            clear_text_widget_fun(pa_text_widget)
    return text_widget_wrapper


@clear_disabled_text_widgets
def clear_text_widget(pa_text_widget):
    pa_text_widget.delete("1.0", "end")


def was_widget_active(pa_widget):
    return pa_widget.cget("state")


def activate_widgets_before_making_changes(*pa_widgets):
    for widget in pa_widgets:
        widget.configure(state="normal")


def deactivate_widgets(*pa_widgets):
    for widget in pa_widgets:
        widget.configure(state="disabled")

