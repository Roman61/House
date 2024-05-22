from Status import StatusDoor


class Door:
    def __init__(self, status=StatusDoor.Close, speed_open=20, current_position=0):

        self.status = status
        self.speed_open = speed_open
        self.current_position = current_position

    def open_door(self):
        self.status = StatusDoor.Opening

    def close_door(self):
        self.status = StatusDoor.Closing

    def update(self):
        if self.status == StatusDoor.Opening:
            self.status = StatusDoor.Open
            return True
        elif self.status == StatusDoor.Closing:
            self.status = StatusDoor.Close
            return True
        elif self.status == StatusDoor.Close:
            return False
        elif self.status == StatusDoor.Open:
            return False

