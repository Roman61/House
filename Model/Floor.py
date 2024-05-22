

class Floor:
    def __init__(self, Number, lift):
        self.number = Number
        self.lift = lift
        self._contains = {}

    def summon_lift(self):
        if self.lift.get_current_floor == self.number:
            self.lift.open_door()
        else:
            self.lift.summon(self.number)

    def drop_to_lift(self, obj):
        my_obj = self._contains.pop(obj)
        if self.lift.push_contains(my_obj):
            return True
        else:
            self._contains[obj] = my_obj
            return False

    def get_from_lift(self, obj):
        self._contains[len(self._contains)] = obj



