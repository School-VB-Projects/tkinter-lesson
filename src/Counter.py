from enum import Enum
from tkinter import Tk, ttk, BooleanVar, IntVar, Frame


class State(Enum):
    """States widgets"""
    SELECTED = 'selected'
    DISABLED = 'disabled'
    NOT_SELECTED = '!selected'
    NOT_DISABLED = '!disabled'


class Default(Enum):
    """Defaults values"""
    FRAME: Frame = None
    COUNT: int = 0
    LOGS = True
    LIMIT: int = 5
    RESET = False
    CHECK_STATE: State = [State.SELECTED.value]
    BUTTON_STATE: State = [State.NOT_DISABLED.value]


class Counter:
    """Counter application"""
    def __init__(self, window: Tk) -> None:
        # https://tkdocs.com/tutorial/concepts.html
        window.title('Counter')
        self.frame: Frame = Default.FRAME.value
        self.compute_frame(window)

        self.enable_logs_default: BooleanVar = BooleanVar(value=bool(Default.LOGS.value))
        self.count: IntVar = IntVar(value=Default.COUNT.value)
        self.limit: IntVar = IntVar(value=Default.LIMIT.value)

        # https://tkdocs.com/tutorial/widgets.html
        self.count_label = ttk.Label(
            self.frame,
            textvariable=self.count,
            font="Poppins"
        )
        self.choose_entry_label = ttk.Label(
            self.frame,
            text="Choose your entry",
            font="Poppins"
        )
        self.custom_entry_label = ttk.Label(
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
            state=State.DISABLED.value
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

    def compute_frame(self, window: Tk) -> None:
        """Configure and compute the frame"""
        ttk.Style().configure('Danger.TFrame', borderwidth=5, relief='sunken')
        self.frame = ttk.Frame(window, padding="20 20 20 20", style='Danger.TFrame')
        self.frame.pack()

    def check_reset(self) -> None:
        """Check if reset is possible and change the button state"""
        if self.count.get() != Default.COUNT.value \
                or self.check.instate([State.NOT_SELECTED.value]) \
                or self.limit.get() != Default.LIMIT.value \
                or self.button.instate([State.DISABLED.value]):
            self.reset.state([State.NOT_DISABLED.value])
        else:
            self.reset.state([State.DISABLED.value])

    def toggle_logs(self) -> None:
        """Enable or disable logs console"""
        if self.check.instate([State.SELECTED.value]):
            print("Enable logs")
        else:
            print("Disable logs")
        self.check_reset()

    def log_if_enabled(self, text: str) -> None:
        """If Enable logs option is enabled, print text in console"""
        if self.check.instate([State.SELECTED.value]):
            print(text)

    def increment(self) -> None:
        """Increment counter (+1) if possible, change state button if not"""
        count: int = self.count.get()
        if count >= self.limit.get():
            self.button.state([State.DISABLED.value])
            self.log_if_enabled("You have reached the limit")
        else:
            self.log_if_enabled("+1")
            self.count.set(count + 1)
        self.check_reset()

    def reset(self) -> None:
        """Reset all values to default values"""
        self.log_if_enabled("Reset values")
        self.count.set(Default.COUNT.value)
        self.check.state(Default.CHECK_STATE.value)
        self.limit.set(Default.LIMIT.value)
        self.button.state(Default.BUTTON_STATE.value)
        self.reset.state([State.DISABLED.value])

    def set_limit(self) -> None:
        """Set limit to requested number"""
        limit: int = self.limit.get()
        if self.count.get() < limit:
            self.button.state([State.NOT_DISABLED.value])
        self.log_if_enabled(f"You have put the limit to {limit}")
        self.check_reset()

    def compute_widgets(self) -> None:
        """Compute all widgets"""
        for widget in self.widgets:
            widget.pack()
