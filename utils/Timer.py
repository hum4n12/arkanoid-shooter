class Timer:

    def __init__(self, time: float, callback: callable) -> None:
        self.original_timer = time
        self.current_time = time
        self.callback = callback
    
    def update(self, dt: float, *args, **kwargs) -> None:
        if self.current_time <= 0.0:
            self.callback(*args, **kwargs)
            self.current_time = self.original_timer
        else:
            self.current_time -= dt

    def reset(self) -> None:
        self.current_time = self.original_timer
