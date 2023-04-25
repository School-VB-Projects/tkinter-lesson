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
        self.frame = None
        window.title('Counter')
        self.compute_frame(window)

        self.enable_logs_default: BooleanVar = BooleanVar(value=bool(Defaults.LOGS.value))

        self.count: IntVar = IntVar(value=Defaults.COUNT.value)
        self.limit = IntVar(value=Defaults.LIMIT.value)

        # https://tkdocs.com/tutorial/widgets.html
        self.count_label: Label = ttk.Label(
            self.frame,
            textvariable=self.count,
            font="Poppins"
        )
        self.choose_entry_label: Label = ttk.Label(
            self.frame,
            text="Choose your entry",
            font="Poppins"
        )
        self.custom_entry_label: Label = ttk.Label(
            self.frame,
            text="Set a custom entry",
            font="Poppins"
        )

        self.button = ttk.Button(
            self.frame,
            text="+1",
            command=self.increment
        )
        self.reset = ttk.Button(
            self.frame,
            text="Reset",
            command=self.reset,
            state=States.DISABLED.value
        )
        self.confirm = ttk.Button(
            self.frame,
            text="Confirm",
            command=self.set_limit
        )

        self.check = ttk.Checkbutton(
            self.frame,
            text='Enable logs',
            command=self.toggle_logs,
            variable=self.enable_logs_default
        )

        self.entry = ttk.Entry(
            self.frame,
            textvariable=self.limit
        )

        self.combobox = ttk.Combobox(
            self.frame,
            textvariable=self.limit,
            values=("5", "10", "15", "20")
        )

        window.bind('<Return>', lambda e: self.button.invoke())

        self.widgets = [
            self.count_label,
            self.button,
            self.reset,
            self.check,
            self.choose_entry_label,
            self.combobox,
            self.custom_entry_label,
            self.entry,
            self.confirm,
        ]

        self.compute_widgets()

        print("History")

    def compute_frame(self, window: Tk):
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame: Frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')
        self.frame.pack()

    def check_reset(self) -> None:
        if self.count.get() != Defaults.COUNT.value \
                or self.check.instate([States.NOT_SELECTED.value]) \
                or self.limit.get() != Defaults.LIMIT.value \
                or self.button.instate([States.DISABLED.value]):
            self.reset.state([States.NOT_DISABLED.value])
        else:
            self.reset.state([States.DISABLED.value])

    def toggle_logs(self) -> None:
        if self.check.instate([States.SELECTED.value]):
            print("Enable logs")
        else:
            print("Disable logs")
        self.check_reset()

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

    def set_limit(self):
        limit = self.limit.get()
        if self.count.get() < limit:
            self.button.state([States.NOT_DISABLED.value])
        self.log_if_enabled(f"You have put the limit to {limit}")
        self.check_reset()

    def compute_widgets(self):
        for widget in self.widgets:
            widget.pack()
