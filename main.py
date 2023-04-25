from tkinter import Tk
from examples.FeetToMeters import FeetToMeters


def run() -> None:
    window = Tk()
    FeetToMeters(window)
    window.mainloop()


if __name__ == '__main__':
    run()
