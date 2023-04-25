from tkinter import Tk, Widget
from typing import Union


# https://tkdocs.com/tutorial/concepts.html
def print_hierarchy(root: Union[Tk, Widget], depth=0) -> None:
    print('  ' * depth + root.winfo_class() + ' w=' + str(root.winfo_width()) + ' h=' + str(
        root.winfo_height()) + ' x=' + str(root.winfo_x()) + ' y=' + str(root.winfo_y()))
    for widget in root.winfo_children():
        print_hierarchy(widget, depth + 1)
