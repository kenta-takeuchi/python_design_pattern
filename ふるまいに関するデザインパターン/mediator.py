import collections


class Form:
    def __init__(self):
        self.create_widgets()
        self.create_mediator()

    def create_widgets(self):
        self.name_text = Text()
        self.email_text = Text()
        self.ok_button = Button("OK")
        self.cancel_button = Button("Cancel")

    def create_mediator(self):
        self.mediator = Mediator(((self.name_text, self.update_ui),
                                  (self.email_text, self.update_ui),
                                  (self.ok_button, self.clicked),
                                  (self.cancel_button, self.clicked)))
        self.update_ui()

    def update_ui(self, widget=None):
        self.ok_button.enabled = (bool(self.name_text.text) and bool(self.email_text.text))

    def clicked(self, widget):
        if widget == self.ok_button:
            print('ok')
        else:
            print('cancel')


class Mediator:
    def __init__(self, widget_callable_pairs):
        self.callables_for_widget = collections.defaultdict(list)
        for widget, caller in widget_callable_pairs:
            self.callables_for_widget[widget].append(caller)
            widget.mediator = self

    def on_change(self, widget):
        callables = self.callables_for_widget.get(widget)
        if callables is not None:
            for caller in callables:
                caller(widget)
        else:
            raise AttributeError(f"No on_change() method registered for {widget}")


class Mediated:
    def __init__(self):
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)


class Button(Mediated):
    def __init__(self, text=''):
        super().__init__()
        self.enabled = True
        self.text = text

    def click(self):
        if self.enabled:
            self.on_change()


class Text(Mediated):
    def __init__(self, text=''):
        super().__init__()
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if self.text != text:
            self.__text = text
            self.on_change()
