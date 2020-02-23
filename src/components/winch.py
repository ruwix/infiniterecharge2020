from utils import lazytalonsrx


class Winch:

    # motor speeds
    HOIST_SPEED = 0.5

    # motor config
    INVERTED = False

    # required devices
    winch_master: lazytalonsrx.LazyTalonSRX

    def __init__(self):
        self.is_hoisting = False
        self.desired_output = 0

    def setup(self):
        self.winch_master.setInverted(self.INVERTED)

    def on_enable(self):
        pass

    def on_disable(self):
        self.stop()

    def hoist(self, output: float) -> None:
        """Hoist up own robot."""
        self.is_hoisting = True
        self.desired_output = self.HOIST_SPEED

    def stop(self) -> None:
        """Stop winch."""
        self.is_hoisting = False
        self.desired_output = 0

    def execute(self):
        if self.is_hoisting:
            self.winch_master.setOutput(self.desired_output)
        else:
            self.winch_master.setOutput(0)