from tkinter import Tk
from examples.FeetToMeters import FeetToMeters
from cli import print_hierarchy


def run() -> None:
    window = Tk()
    FeetToMeters(window)
    print_hierarchy(window)
    window.mainloop()


if __name__ == '__main__':
    run()
