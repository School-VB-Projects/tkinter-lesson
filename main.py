from tkinter import Tk
from src.Counter import Counter


def run() -> None:
    window = Tk()
    Counter(window)
    window.mainloop()


if __name__ == '__main__':
    run()
