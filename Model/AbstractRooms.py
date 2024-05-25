class AbstractRooms:
    def __init__(self, name='', Number=0, height=0, status=None, door=None, hendler=None):
        self.name = name
        self.number = Number
        self.height = height
        self.status = status
        self.action_for_user = []
        self.action_for_system = []
        self._contains = {}
        self.door = door

        #print("Инициализатор класса AbstractRooms")

    def get_action_for_user(self):
        _dist = {"open_door": self.open_door, 'close_door': self.close_door}
        self.action_for_user.append(_dist)
        return self.action_for_user

    def get_action_for_system(self):
        _dist = {"update": self.update}
        self.action_for_system.append(_dist)
        return self.action_for_system

    def update(self):
        raise Exception(f"Method Update() in {self.__class__.__name__} undefined!")

    def open_door(self):
        self.door.open_door()

    def close_door(self):
        self.door.close_door()
