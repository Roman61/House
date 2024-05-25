from datetime import datetime

from Model.Status import StatusDoor
from EventsSystem.Events import Hendlers


class Door:
    def __init__(self, name='', status=StatusDoor.Close, speed_open=20, current_position=0, hendler=None):
        self.status = status
        self.speed_open = speed_open
        self.current_position = current_position
        self.name = name
        if hendler is None:
            self.hendler = Hendlers()
        else:
            self.hendler = hendler

        self.event_opening = None
        self.event_closing = None
        self.event_close = None
        self.event_open = None

    def event_binding(self):
        self.hendler.hendler('event_door_is_opening', self.event_opening)
        self.hendler.hendler('event_door_is_closing', self.event_closing)
        self.hendler.hendler('event_door_is_close', self.event_close)
        self.hendler.hendler('event_door_is_open', self.event_open)
        self.hendler.hendler('update', self.update)

    def open_door(self):
        self.status = StatusDoor.Opening

    def close_door(self):
        self.status = StatusDoor.Closing

    def update(self, current=datetime.now()):
        if self.status == StatusDoor.Opening:
            self.status = StatusDoor.Open
            if self.event_opening is not None:
                self.hendler.dispactch('event_door_is_opening', self.name)
            # print('Двери открываются')
            # return False
        elif self.status == StatusDoor.Closing:
            self.status = StatusDoor.Close
            if self.event_closing is not None:
                self.hendler.dispactch('event_door_is_closing', self.name)
            # print('Двери закрываются')
            # return False
        elif self.status == StatusDoor.Close:
            self.status = StatusDoor.finish
            if self.event_close is not None:
                self.hendler.dispactch('event_door_is_close', self.name)
            # print('Двери закрыты')
            # return True
        elif self.status == StatusDoor.Open:
            self.status = StatusDoor.finish
            if self.event_open is not None:
                self.hendler.dispactch('event_door_is_open', self.name)
            # print('Двери открыты')
            # return True
