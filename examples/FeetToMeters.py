from tkinter import ttk, Tk, StringVar, W, E


# https://tkdocs.com/tutorial/firstexample.html
class FeetToMeters:

    def __init__(self, root: Tk):
        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky="N W E S")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky="W E")
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky="W E")
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind('<Return>', lambda e: self.calculate())  # https://tkdocs.com/tutorial/concepts.html

    def calculate(self) -> None:
        try:
            self.meters.set(str(int(0.3048 * float(self.feet.get()) * 10000.0 + 0.5) / 10000.0))
        except ValueError:
            pass
