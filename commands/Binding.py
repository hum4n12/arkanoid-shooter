class Binding:

    def __init__(self, action: int, command: callable) -> None:
        self._action: int = action
        self._command: callable = command

    @property
    def action(self):
        return self._action

    def execute(self) -> None:
        self._command()
