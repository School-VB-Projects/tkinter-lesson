from tkinter import Tk, ttk, StringVar


class Test:
    def __init__(self, window: Tk):
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Test')

        # https://tkdocs.com/tutorial/widgets.html
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')

        frame.pack()

        self.count = 0
        self.text = StringVar()
        self.text.set(str(self.count))

        label = ttk.Label(frame, textvariable=self.text, font="Poppins")
        button = ttk.Button(frame, text="+1", default="active", command=self.test)

        window.bind('<Return>', lambda e: button.invoke())

        label.pack()
        button.pack()

    def test(self):
        print("+1")
        self.count += 1
        self.text.set(str(self.count))
        print(self.count, self.text)
