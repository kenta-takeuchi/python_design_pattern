import sys

if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape

WINNERS = ("Nikolai Andrianov", "Matt Biondi", "Bjørn Dæhlie",
           "Birgit Fischer", "Sawao Kato", "Larisa Latynina", "Carl Lewis",
           "Michael Phelps", "Mark Spitz", "Jenny Thompson")


def main():
    html_layout = Layout(html_tabulator)
    for rows in range(2, 6):
        print(html_layout.tabulate(rows, WINNERS))
    text_layout = Layout(text_tabulator)
    for rows in range(2, 6):
        print(text_layout.tabulate(rows, WINNERS))


class Layout:
    def __init__(self, tabulator):
        self.tabulator = tabulator

    def tabulate(self, rows, items):
        return self.tabulator(rows, items)


def html_tabulator(rows, items):
    columns, remainder = divmod(len(items), rows)
    if remainder:
        columns += 1
    column = 0
    table = ['<table border="1">\n']
    for item in items:
        if column == 0:
            table.append("<tr>")
        table.append("<td>{}</td>".format(escape(str(item))))
        column += 1
        if column == columns:
            table.append("</tr>\n")
        column %= columns
    if table[-1][-1] != "\n":
        table.append("</tr>\n")
    table.append("</table>\n")
    return "".join(table)


def text_tabulator(rows, items):
    columns, remainder = divmod(len(items), rows)
    if remainder:
        columns += 1
        remainder = (rows * columns) - len(items)
        if remainder == columns:
            remainder = 0
    column = column_width = 0
    for item in items:
        column_width = max(column_width, len(item))
    column_divider = ("-" * (column_width + 2)) + "+"
    divider = "+" + (column_divider * columns) + "\n"
    table = [divider]
    for item in items + (("",) * remainder):
        if column == 0:
            table.append("|")
        table.append(" {:<{}} |".format(item, column_width))
        column += 1
        if column == columns:
            table.append("\n")
        column %= columns
    table.append(divider)
    return "".join(table)


if __name__ == "__main__":
    main()
