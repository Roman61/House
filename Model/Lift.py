from datetime import datetime
from Model.Door import Door
from Model.Singleton import Singleton
from Model.Status import StatusLift, StatusDoor

from Model.Obj import Object


class Lift(metaclass=Singleton):
    def __init__(self, shaft_height, max_speed, max_weight=400, current_position=0, current_Floor=1, current_speed=0,
                 time_stop=None, attached_floor=None, time_start=None, current_time=None, status=StatusLift.stand,
                 target_Floor=0, door=Door()):
        """
        :param shaft_height: Высота шахты лифта
        :param max_speed: Скорость перемещения лифта
        """
        self.max_weight = max_weight
        self._index_current_floor = current_Floor
        self._current_position = current_position
        self._current_speed = current_speed
        self._time_start = time_start
        self._current_time = current_time
        self.time_stop = time_stop
        self.shaft_height = shaft_height
        self.speed = max_speed
        self._status = status
        self._index_target_floor = target_Floor
        self._door = door
        self._contains = {}
        self._attached_floor = attached_floor

    def attachment_floor(self, floor):
        self._attached_floor = floor

    def stop(self):
        self._status = StatusLift.stand

    def push_contains(self, obj):
        summa = 0
        for i in self._contains:
            summa += i.weight
        if summa + obj.weight < self.max_weight:
            self._contains[len(self._contains)] = obj
            return True
        else:
            return False

    def update(self, current=datetime.now()):
        self._attached_floor = None
        self._current_time = current
        # print(f'{self._current_time.hour}:{self._current_time.minute}:{self._current_time.second}')
        if self._door.status == StatusDoor.Close:
            if self._status == StatusLift.go_up:
                if self._index_current_floor == self._index_target_floor:
                    self._status = StatusLift.stand
                    self.open_door()
                else:
                    self._index_current_floor += 1
                    print(f'Текущий этаж: {self._index_current_floor}')
            elif self._status == StatusLift.go_down:
                if self._index_current_floor == self._index_target_floor:
                    self._status = StatusLift.stand
                    self.open_door()
                else:
                    self._index_current_floor -= 1
                    print(f'Текущий этаж: {self._index_current_floor}')
            elif self._status == StatusLift.stand:
                if self._door.status == StatusDoor.Close:
                    print('Лифт приехал')
                else:
                    return self._door.update()
        else:
            return self._door.update()
        return False

    def open_door(self):
        self._door.open_door()

    def close_door(self):
        self._attached_floor = None
        self._door.close_door()

    def get_current_floor(self):
        return self._index_current_floor

    def go_to_floor(self, target):
        self._index_target_floor = target
        self._go()
        self._door.close_door()

    def summon(self, target):
        self._index_target_floor = target
        print(f"Вызываем лифт")
        self._go()

    def _go(self):
        if self._index_target_floor > self._index_current_floor:
            self._up()
        elif self._index_target_floor < self._index_current_floor:
            self._down()
        elif self._index_target_floor == self._index_current_floor:
            self.open_door()
        print(f"текущий этаж {self._index_current_floor}")

    def _up(self):
        print("Едем вверх,", end=' ')
        self._status = StatusLift.go_up
        self._time_start = datetime.now()

    def _down(self):
        print("Едем вниз,", end=' ')
        self._status = StatusLift.go_down
        self._time_start = datetime.now()
