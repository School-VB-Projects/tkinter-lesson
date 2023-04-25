from tkinter import Tk, ttk, PhotoImage, BooleanVar, IntVar, Frame, Label


class Test:
    def __init__(self, window: Tk) -> None:
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Test')

        # https://tkdocs.com/tutorial/widgets.html
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame: Frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')

        self.frame.pack()

        self.count: IntVar = IntVar(value=0)
        self.image: PhotoImage = PhotoImage(file='assets/pycharm.png')
        self.enable_logs_default: BooleanVar = BooleanVar(value=True)

        self.picture: Label = ttk.Label(image=self.image)
        self.label: Label = ttk.Label(self.frame, textvariable=self.count, font="Poppins")
        self.button = ttk.Button(self.frame, text="+1", default="active", command=self.test)
        self.check = ttk.Checkbutton(self.frame, text='Enable logs',
                                     command=self.toggle_logs, variable=self.enable_logs_default)

        window.bind('<Return>', lambda e: self.button.invoke())

        # self.picture.pack()
        self.label.pack()
        self.button.pack()
        self.check.pack()

    def test(self) -> None:
        count = self.count.get()
        if count >= 10:
            print("You have reached the limit")
            self.button.state(['disabled'])
        else:
            if self.check.instate(['selected']):
                print("+1")
            self.count.set(count + 1)
            # print(f"Count: {self.count}")

    def toggle_logs(self) -> None:
        if self.check.instate(['selected']):
            print("Enable logs")
        else:
            print("Disable logs")
