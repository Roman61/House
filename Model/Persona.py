class Persona:
    def __init__(self, weight, Name):
        self.weight = weight
        self.name = Name
        self.room = None

    def attachment_room(self, room):
        self.room = room

    def object_to_lift(self):
        pass

        # if isinstance(obj, str):
        #     pass
        # elif isinstance(obj, int):
        #     my_obj = self._contains[obj]
        #     if self.lift.push_contains(my_obj):
        #         del self._contains[self._contains[obj]]
        #         return True
        #     else:
        #         self._contains[obj] = my_obj
        #         return False
        # elif isinstance(obj, Object):
        #     my_obj = self._contains.pop(obj)
        #     if self.lift.push_contains(my_obj):
        #         return True
        #     else:
        #         self._contains[obj] = my_obj
        #         return False
        # else:
        #     return False
    def object_to_parent(self):
        pass
            # self._contains[len(self._contains)] =

    def get_obj_from(self, obj):
            # self._contains[len(self._contains)] = obj
        pass
