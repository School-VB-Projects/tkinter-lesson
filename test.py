from tkinter import Tk, ttk, StringVar, PhotoImage, BooleanVar


class Test:
    def __init__(self, window: Tk):
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Test')

        # https://tkdocs.com/tutorial/widgets.html
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')

        self.frame.pack()

        self.count = 0
        self.text = StringVar(value=str(self.count))
        self.image = PhotoImage(file='assets/pycharm.png')
        self.enable_logs_default = BooleanVar(value=True)

        self.picture = ttk.Label(image=self.image)
        self.label = ttk.Label(self.frame, textvariable=self.text, font="Poppins")
        self.button = ttk.Button(self.frame, text="+1", default="active", command=self.test)
        self.check = ttk.Checkbutton(self.frame, text='Enable logs',
                                     command=self.toggle_logs, variable=self.enable_logs_default)

        window.bind('<Return>', lambda e: self.button.invoke())

        # self.picture.pack()
        self.label.pack()
        self.button.pack()
        self.check.pack()

    def test(self):
        if self.count >= 10:
            print("You have reached the limit")
            self.button.state(['disabled'])
            pass
        else:
            if self.check.instate(['selected']):
                print("+1")
            self.count += 1
            self.text.set(str(self.count))
            # print(f"Count: {self.count}")

    def toggle_logs(self):
        if self.check.instate(['selected']):
            print("Enable logs")
        else:
            print("Disable logs")
