from tkinter import Tk, ttk, StringVar, PhotoImage


class Test:
    def __init__(self, window: Tk):
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Test')

        # https://tkdocs.com/tutorial/widgets.html
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')

        self.frame.pack()

        self.count = 0
        self.text = StringVar()
        self.text.set(str(self.count))
        self.image = PhotoImage(file='assets/pycharm.png')

        self.picture = ttk.Label(image=self.image)
        self.label = ttk.Label(self.frame, textvariable=self.text, font="Poppins")
        self.button = ttk.Button(self.frame, text="+1", default="active", command=self.test)

        window.bind('<Return>', lambda e: self.button.invoke())

        # self.picture.pack()
        self.label.pack()
        self.button.pack()

    def test(self):
        if self.count >= 10:
            print("ERROR: You have reached the limit")
            self.button.state(['disabled'])
            pass
        else:
            print("+1")
            self.count += 1
            self.text.set(str(self.count))
            # print(f"Count: {self.count}")

