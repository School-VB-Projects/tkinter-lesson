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
        self.enable_logs_default: BooleanVar = BooleanVar(value=True)
        self.limit = IntVar(value=5)

        self.label: Label = ttk.Label(self.frame, textvariable=self.count, font="Poppins")
        self.button = ttk.Button(self.frame, text="+1", default="active", command=self.test)
        self.reset = ttk.Button(self.frame, text="Reset", default="active", command=self.reset)
        self.limit_5 = ttk.Radiobutton(self.frame, text='Put limit to 5', variable=self.limit, value=5,
                                       command=self.put_limit)
        self.limit_10 = ttk.Radiobutton(self.frame, text='Put limit to 10', variable=self.limit, value=10,
                                        command=self.put_limit)
        self.check = ttk.Checkbutton(self.frame, text='Enable logs',
                                     command=self.toggle_logs, variable=self.enable_logs_default)

        window.bind('<Return>', lambda e: self.button.invoke())

        self.label.pack()
        self.button.pack()
        self.reset.pack()
        self.check.pack()
        self.limit_5.pack()
        self.limit_10.pack()

    def test(self) -> None:
        count = self.count.get()
        if count >= self.limit.get():
            print("You have reached the limit")
            self.button.state(['disabled'])
        else:
            if self.check.instate(['selected']):
                print("+1")
            self.count.set(count + 1)

    def reset(self) -> None:
        self.count.set(0)
        self.check.state(['selected'])
        self.limit.set(5)
        self.button.state(['!disabled'])
        print("Reset")

    def toggle_logs(self) -> None:
        if self.check.instate(['selected']):
            print("Enable logs")
        else:
            print("Disable logs")

    def put_limit(self) -> None:
        print(f"You have put the limit to {self.limit.get()}")
