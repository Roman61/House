from Model.Obj import Object


class Floor:
    def __init__(self, Number=0, lift=None, parent=None, child=None):
        self.number = Number
        self.lift = lift
        self._contains = {}
        self.parent = parent
        self.child = child

    def attachment_parent(self, parent):
        self.parent = parent

    def attachment_child(self, child):
        self.child = child

    def summon_lift(self):
        if self.lift.get_current_floor == self.number:
            self.lift.open_door()
        else:
            self.lift.summon(self.number)




