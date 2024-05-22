from datetime import datetime
from Model.Singleton import Singleton
from Model.Status import StatusLift, StatusDoor
from Model.Door import Door
from Model.Obj import Object


class Lift(metaclass=Singleton):
    def __init__(self, shaft_height, max_speed, max_weight=400, current_position=0, current_Floor=1, current_speed=0,
                 time_stop=None,
                 time_start=None, current_time=None, status=StatusLift.stand, target_Floor=0, door=Door()):
        """
        :param shaft_height: Высота шахты лифта
        :param max_speed: Скорость перемещения лифта
        """
        self.max_weight = max_weight
        self._current_floor = current_Floor
        self._current_position = current_position
        self._current_speed = current_speed
        self._time_start = time_start
        self._current_time = current_time
        self.time_stop = time_stop
        self.shaft_height = shaft_height
        self.speed = max_speed
        self._status = status
        self._target_floor = target_Floor
        self._door = door
        self._contains = {}

    def stop(self):
        self._status = StatusLift.stand

    def push_contains(self, obj):
        summa = 0
        for i in self._contains:
            summa += Object(i).weight
        if summa + Object(obj).weight < self.max_weight:
            self._contains[len(self._contains)] = obj
            return True
        else:
            return False

    def update(self, current=datetime.now()):
        self._current_time = current
        print(f'{self._current_time.hour}:{self._current_time.minute}:{self._current_time.second}')
        if self._status == StatusLift.go_up:
            if self._current_floor == self._target_floor:
                self._status = StatusLift.stand
                self.open_door()
            else:
                self._current_floor += 1
        elif self._status == StatusLift.go_down:
            if self._current_floor == self._target_floor:
                self._status = StatusLift.stand
                self.open_door()
            else:
                self._current_floor -= 1
        elif self._status == StatusLift.stand:
            return self._door.update()
        return False

    def open_door(self):
        self._door.open_door()

    def close_door(self):
        self._door.close_door()

    def get_current_floor(self):
        return self._current_floor

    def go_to_floor(self, target):
        self._target_floor = target

    def summon(self, target):
        self._target_floor = target

    def _up(self):
        self._status = StatusLift.go_up
        self._time_start = datetime.now()

    def _down(self):
        self._status = StatusLift.go_down
        self._time_start = datetime.now()
