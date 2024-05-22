import enum


class StatusLift(enum.Enum):
    stand = 0
    go_up = 1
    go_down = 2


class StatusDoor(enum.Enum):
    Close = 0
    Open = 1
    Opening = 2
    Closing = 3
