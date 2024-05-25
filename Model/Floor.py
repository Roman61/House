from Model.Persona import Persona
from Model.AbstractRooms import AbstractRooms as room


class Floor(room):
    def __init__(self, Number=0, lift=None, parent=None, child=None, name='этаж'):
        super().__init__(name=name, Number=Number)
        # self.number = Number
        # self.name = name
        # self.action_for_user = []
        # self._contains = {}

        self.lift = lift
        self.parent = parent
        self.child = child

    def get_actions_for_user(self):
        _dist = {"summon": self.summon_lift}
        self.action_for_user.append(_dist)
        return self.action_for_user

    def attachment_parent(self, parent):
        self.parent = parent

    def attachment_child(self, child):
        self.child = child

    def summon_lift(self):
        if self.lift.get_current_floor == self.number:
            self.lift.open_door()
        else:
            self.lift.summon(self.number)
