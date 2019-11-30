import abc
import sys
if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape


def main():
    html_form = create_login_form(HtmlFormBuilder())
    print("wrote", html_form)

    print("-----")

    html_input = create_input(HtmlInputBuilder())
    print("wrote", html_input)


def create_login_form(builder):
    builder.add_title("Login")
    builder.add_label("Username", 0, 0, target="username")
    builder.add_entry("username", 0, 1)
    builder.add_label("Password", 1, 0, target="password")
    builder.add_entry("password", 1, 1, kind="password")
    builder.add_button("Login", 2, 0)
    builder.add_button("Cancel", 2, 1)
    return builder.form()


def create_input(builder):
    builder.add_id("input")
    builder.add_name("input")
    builder.add_type("text")
    builder.add_placeholder("名前を入力してください")
    return builder.input()


class AbstractFormBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_title(self, title):
        pass

    @abc.abstractmethod
    def form(self):
        pass

    @abc.abstractmethod
    def add_label(self, text, row, column, **kwargs):
        pass

    @abc.abstractmethod
    def add_entry(self, variable, row, column, **kwargs):
        pass

    @abc.abstractmethod
    def add_button(self, text, row, column, **kwargs):
        pass


class AbstractElementBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_id(self, element_id):
        pass

    @abc.abstractmethod
    def input(self):
        pass

    @abc.abstractmethod
    def add_name(self, name):
        pass

    @abc.abstractmethod
    def add_class(self, element_class):
        pass


class HtmlFormBuilder(AbstractFormBuilder):

    def __init__(self):
        self.title = "HtmlFormBuilder"
        self.items = {}

    def add_title(self, title):
        self.title = escape(title)

    def add_label(self, text, row, column, **kwargs):
        self.items[(row, column)] = ('<td><label for="{}">{}:</label></td>'.format(kwargs["target"], escape(text)))

    def add_entry(self, variable, row, column, **kwargs):
        html = """<td><input name="{}" type="{}" /></td>""".format(
                variable, kwargs.get("kind", "text"))
        self.items[(row, column)] = html

    def add_button(self, text, row, column, **kwargs):
        html = """<td><input type="submit" value="{}" /></td>""".format(
                escape(text))
        self.items[(row, column)] = html

    def form(self):
        html = ["<!doctype html>\n<html><head><title>{}</title></head>"
                "<body>".format(self.title), '<form><table border="0">']
        this_row = None
        for key, value in sorted(self.items.items()):
            row, column = key
            if this_row is None:
                html.append("  <tr>")
            elif this_row != row:
                html.append("  </tr>\n  <tr>")
            this_row = row
            html.append("    " + value)
        html.append("  </tr>\n</table></form></body></html>")
        return "\n".join(html)


class HtmlInputBuilder(AbstractElementBuilder):

    def __init__(self):
        self.input_id = None
        self.name = None
        self.input_class = None
        self.input_type = None
        self.value = None
        self.placeholder = None

    def add_id(self, input_id):
        self.input_id = escape(input_id)

    def add_name(self, name):
        self.name = escape(name)

    def add_class(self, input_class):
        self.input_class = escape(input_class)

    def add_type(self, input_type):
        self.input_type = escape(input_type)

    def add_value(self, value):
        self.value = escape(value)

    def add_placeholder(self, placeholder):
        self.placeholder = escape(placeholder)

    def input(self):
        input_text = ""
        if self.input_id:
            input_text += ' id="{}"'.format(self.input_id)
        if self.name:
            input_text += ' name="{}"'.format(self.name)
        if self.input_class:
            input_text += ' type="{}"'.format(self.input_class)
        if self.input_type:
            input_text += ' type="{}"'.format(self.input_type)
        if self.value:
            input_text += ' value="{}"'.format(self.value)
        if self.placeholder:
            input_text += ' placeholder="{}"'.format(self.placeholder)

        return "<input{}>".format(input_text)


if __name__ == "__main__":
    main()
