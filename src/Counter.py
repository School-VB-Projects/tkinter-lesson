from enum import Enum
from tkinter import Tk, ttk, BooleanVar, IntVar, Frame, Label


class States(Enum):
    SELECTED = 'selected'
    DISABLED = 'disabled'
    NOT_SELECTED = '!selected'
    NOT_DISABLED = '!disabled'


class Defaults(Enum):
    COUNT: int = 0
    LOGS: bool = True
    LIMIT: int = 5
    RESET: bool = False
    CHECK_STATE = [States.SELECTED.value]
    BUTTON_STATE = [States.NOT_DISABLED.value]


class Counter:
    def __init__(self, window: Tk) -> None:
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Counter')

        # https://tkdocs.com/tutorial/widgets.html
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame: Frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')

        self.frame.pack()

        self.enable_logs_default: BooleanVar = BooleanVar(value=bool(Defaults.LOGS.value))

        self.count: IntVar = IntVar(value=Defaults.COUNT.value)
        self.limit = IntVar(value=Defaults.LIMIT.value)

        self.label: Label = ttk.Label(self.frame, textvariable=self.count, font="Poppins")
        self.button = ttk.Button(self.frame, text="+1", command=self.increment)
        self.reset = ttk.Button(self.frame, text="Reset", command=self.reset, state=States.DISABLED.value)
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

    def check_reset(self) -> None:
        if self.count.get() != Defaults.COUNT.value or self.check.instate(
                [States.NOT_SELECTED.value]) or self.limit.get() != Defaults.LIMIT.value or self.button.instate(
                [States.DISABLED.value]):
            self.reset.state([States.NOT_DISABLED.value])
        else:
            self.reset.state([States.DISABLED.value])

    def log_if_enabled(self, text: str) -> None:
        if self.check.instate([States.SELECTED.value]):
            print(text)

    def increment(self) -> None:
        count = self.count.get()
        if count >= self.limit.get():
            self.button.state([States.DISABLED.value])
            self.log_if_enabled("You have reached the limit")
        else:
            self.log_if_enabled("+1")
            self.count.set(count + 1)
        self.check_reset()

    def reset(self) -> None:
        self.log_if_enabled("Reset values")
        self.count.set(Defaults.COUNT.value)
        self.check.state(Defaults.CHECK_STATE.value)
        self.limit.set(Defaults.LIMIT.value)
        self.button.state(Defaults.BUTTON_STATE.value)
        self.reset.state([States.DISABLED.value])

    def toggle_logs(self) -> None:
        if self.check.instate([States.SELECTED.value]):
            print("Enable logs")
        else:
            print("Disable logs")
        self.check_reset()

    def put_limit(self) -> None:
        if self.count.get() < self.limit.get():
            self.button.state([States.NOT_DISABLED.value])
        self.log_if_enabled(f"You have put the limit to {self.limit.get()}")
        self.check_reset()
