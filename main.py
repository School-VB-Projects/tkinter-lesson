from tkinter import Tk
# from examples.FeetToMeters import FeetToMeters
from src.Counter import Counter


def run() -> None:
    window = Tk()
    # FeetToMeters(window)
    Counter(window)
    # print_hierarchy(window)
    print("History")
    window.mainloop()


if __name__ == '__main__':
    run()
