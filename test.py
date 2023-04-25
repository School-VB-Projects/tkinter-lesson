from enum import Enum
from tkinter import Tk, ttk, PhotoImage, BooleanVar, IntVar, Frame, Label


class States(Enum):
    SELECTED = 'selected'
    DISABLED = 'disabled'
    ENABLED = '!disabled'


class Defaults(Enum):
    COUNT: int = 0
    LOGS: bool = True
    LIMIT: int = 5
    CHECK_STATE = [States.SELECTED.value]
    BUTTON_STATE = [States.ENABLED.value]


class Test:
    def __init__(self, window: Tk) -> None:
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Test')

        # https://tkdocs.com/tutorial/widgets.html
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame: Frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')

        self.frame.pack()

        self.enable_logs_default: BooleanVar = BooleanVar(value=bool(Defaults.LOGS.value))

        self.count: IntVar = IntVar(value=Defaults.COUNT.value)
        self.limit = IntVar(value=Defaults.LIMIT.value)

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

    def log_if_enabled(self, text: str) -> None:
        if self.check.instate([States.SELECTED.value]):
            print(text)

    def test(self) -> None:
        count = self.count.get()
        if count >= self.limit.get():
            self.button.state([States.DISABLED.value])
            self.log_if_enabled("You have reached the limit")
        else:
            self.log_if_enabled("+1")
            self.count.set(count + 1)

    def reset(self) -> None:
        self.count.set(Defaults.COUNT.value)
        self.check.state(Defaults.CHECK_STATE.value)
        self.limit.set(Defaults.LIMIT.value)
        self.button.state(Defaults.BUTTON_STATE.value)
        self.log_if_enabled("Reset values")

    def toggle_logs(self) -> None:
        if self.check.instate([States.SELECTED.value]):
            print("Enable logs")
        else:
            print("Disable logs")

    def put_limit(self) -> None:
        self.log_if_enabled(f"You have put the limit to {self.limit.get()}")
