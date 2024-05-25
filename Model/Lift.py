from datetime import datetime
from EventsSystem.Events import Hendlers
from Model.AbstractRooms import AbstractRooms
from Model.Door import Door
from Helpers.Singleton import singleton
from Model.Status import StatusLift, StatusDoor


class Lift(AbstractRooms):
    def __init__(self, shaft_height, max_speed, max_weight=400, current_position=0, current_Floor=1, current_speed=0,
                 time_stop=None, attached_floor=None, time_start=None, current_time=None, status=StatusLift.stand,
                 target_Floor=0, door=None, Number=0, name='', hendler=None):
        """
        :param shaft_height:
        :param max_speed:
        :param max_weight:
        :param current_position:
        :param current_Floor:
        :param current_speed:
        :param time_stop:
        :param attached_floor:
        :param time_start:
        :param current_time:
        :param status:
        :param target_Floor:
        :param door:
        :param Number:
        :param name:
        :param hendler:
        """
        super().__init__(name=name, status=status, Number=Number, door=door)
        # self._status = status
        # self._door = door

        # self._contains = {}
        # self.action_for_user = []
        if hendler is None:
            self.hendler = Hendlers()
        else:
            self.hendler = hendler
        self.speed = max_speed
        self._current_speed = current_speed
        self._time_start = time_start
        self._current_time = current_time
        self.time_stop = time_stop
        self.shaft_height = shaft_height
        self._attached_floor = attached_floor
        self._index_target_floor = target_Floor
        self.max_weight = max_weight
        self._index_current_floor = current_Floor
        self._current_position = current_position
        self.event_current = None
        self.event_done = None
        self.event_selected = None
        self.event_summon = None
        self.event_move_to_up = None
        self.event_move_to_down = None
        self.event_door_opening = None
        self.event_door_closing = None
        self.event_door_close = None
        self.event_door_open = None

    def event_binding(self):
        self._door.event_opening = self.event_door_opening
        self._door.event_closing = self.event_door_closing
        self._door.event_close = self.event_door_close
        self._door.event_open = self.event_door_open

        self.hendler.hendler('Lift_move', self.event_current)
        self.hendler.hendler('Lift_done', self.event_done)
        self.hendler.hendler('Lift_select', self.event_selected)
        self.hendler.hendler('Lift_summon', self.event_summon)
        self.hendler.hendler('Lift_up', self.event_move_to_up)
        self.hendler.hendler('Lift_down', self.event_move_to_down)
        self.hendler.hendler('door_opening', self.event_door_opening)
        self.hendler.hendler('door_closing', self.event_door_closing)
        self.hendler.hendler('door_close', self.event_door_close)
        self.hendler.hendler('door_open', self.event_door_open)

    def get_action_for_user(self):
        _dist = {"summon": self.summon, }
        self.action_for_user.append(_dist)
        return self.action_for_user

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
                    # self.open_door()
                else:
                    self._index_current_floor += 1
                    if self.event_current is not None:
                        self.hendler.dispactch('Lift_move', {'name': self.name, 'current': self._index_current_floor,
                                                             'target': self._index_target_floor})
                    # print(f'Текущий {self.name}: {self._index_current_floor}')
            elif self._status == StatusLift.go_down:
                if self._index_current_floor == self._index_target_floor:
                    self._status = StatusLift.stand
                else:
                    self._index_current_floor -= 1
                    if self.event_current is not None:
                        self.hendler.dispactch('Lift_move', {'name': self.name, 'current': self._index_current_floor,
                                                             'target': self._index_target_floor})
                    # print(f'Текущий {self.name}: {self._index_current_floor}')
            elif self._status == StatusLift.stand:
                if self._door.status == StatusDoor.Close:
                    if self.event_done is not None:
                        self.hendler.dispactch('Lift_done', {'name': self.name, 'current': self._index_current_floor,
                                                             'target': self._index_target_floor})
                    # print(f'{self.name} приехал')
                    self.open_door()
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
        # print(f'Выбран этаж: {target}')
        self._index_target_floor = target
        if self.event_selected is not None:
            self.hendler.dispactch('Lift_select', {'name': self.name, 'current': self._index_current_floor,
                                                   'target': self._index_target_floor})

        self._go()
        self._door.close_door()

    def summon(self, target):
        self._index_target_floor = target
        # print(f"Вызываем лифт")
        if self.event_summon is not None:
            self.hendler.dispactch('Lift_summon', {'name': self.name, 'current': self._index_current_floor,
                                                   'target': self._index_target_floor})
        self._go()

    def _go(self):
        if self._index_target_floor > self._index_current_floor:
            self._up()
        elif self._index_target_floor < self._index_current_floor:
            self._down()
        elif self._index_target_floor == self._index_current_floor:
            self.open_door()
        if self.event_current is not None:
            self.hendler.dispactch('Lift_move', {'name': self.name, 'current': self._index_current_floor,
                                                 'target': self._index_target_floor})
        # print(f"текущий этаж {self._index_current_floor}")

    def _up(self):
        if self.event_move_to_up is not None:
            self.hendler.dispactch('Lift_up', {'name': self.name, 'current': self._index_current_floor,
                                               'target': self._index_target_floor})
        # print(f"Едем вверх на {self._index_target_floor},", end=' ')
        self._status = StatusLift.go_up
        self._time_start = datetime.now()

    def _down(self):
        if self.event_move_to_down is not None:
            self.hendler.dispactch('Lift_down', {'name': self.name, 'current': self._index_current_floor,
                                                 'target': self._index_target_floor})
        # print(f"Едем вниз на {self._index_target_floor},", end=' ')
        self._status = StatusLift.go_down
        self._time_start = datetime.now()
