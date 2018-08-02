# TODO apply decorator to work on disabled text widgets as well
def fill_text_box(pa_text_widget, pa_items):
    # TODO remove this line and add the abovementioned functionality via a decorator

    was_active = was_widget_active(pa_text_widget)
    if was_active != "normal":
        activate_widgets_before_making_changes(pa_text_widget)

    for item in pa_items:
        item += "\n"
        pa_text_widget.insert("end", item)

    if was_active != "normal":
        deactivate_widgets(pa_text_widget)


def clear_text_widgets(*pa_widgets):
    for widget in pa_widgets:
        clear_text_widget(widget)


def clear_disabled_text_widget(clear_text_widget_fun):
    def text_widget_wrapper(pa_text_widget):
        was_active = was_widget_active(pa_text_widget)
        if was_active  != "normal":
            activate_widgets_before_making_changes(pa_text_widget)

        clear_text_widget_fun(pa_text_widget)

        if was_active != "normal":
            deactivate_widgets(pa_text_widget)
    return text_widget_wrapper


@clear_disabled_text_widget
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

