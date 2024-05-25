from Model.Door import Door
from Model.Floor import Floor
from Model.Lift import Lift
from Model.Status import StatusDoor, StatusLift
from Viewer.Printer import LiftPrinter, DoorPrinter


class House:
    def __init__(self, height, max_of_floors):
        self.height = height

        self.maxOfFloors = max_of_floors
        door = Door(name="двери лифта")
        self.lift = Lift(self.height, 20, name='Лифт', door=door, house=self)
        self.lift.event_current = LiftPrinter.pr_current
        self.lift.event_done = LiftPrinter.pr_done
        self.lift.event_selected = LiftPrinter.pr_selected
        self.lift.event_select_error = LiftPrinter.pr_selected_error
        self.lift.event_move_to_up = LiftPrinter.pr_move_to_up
        self.lift.event_move_to_down = LiftPrinter.pr_move_to_down
        self.lift.event_summon = LiftPrinter.pr_summon
        self.lift.event_door_open = DoorPrinter.pr_open
        self.lift.event_door_close = DoorPrinter.pr_close

        self.lift.event_door_opening = DoorPrinter.pr_opening
        self.lift.event_door_closing = DoorPrinter.pr_closing

        self.lift.event_binding()
        self.floors = []
        self.floors.append(Floor(Number=1, lift=self.lift))
        self.lift.attachment_floor()  # self.floors[len(self.floors) - 1]
        for j in range(2, self.maxOfFloors + 1):
            self.floors.append(Floor(Number=j, lift=self.lift))
            count = len(self.floors) - 1
            parent = self.floors[count - 1]
            current = self.floors[count]
            current.attachment_parent(parent)
            parent.attachment_child(current)

        print(f'В доме {len(self.floors)} этажей')


# Тест
if __name__ == '__main__':
    house = House(height=400, max_of_floors=10)

    var = house.floors[9].get_actions_for_user()
    for i in var:
        i['summon']()
    while True:
        house.lift.hendler.dispactch('update', None)
        if house.lift.door.status == StatusDoor.finish and house.lift.status == StatusLift.finish:
            house.lift.hendler.dispactch('update', None)
            # house.lift.attachment_floor(house.floors[9])
            break

    house.lift.go_to_floor(1)
    while True:
        house.lift.hendler.dispactch('update', None)
        if house.lift.door.status == StatusDoor.finish and house.lift.status == StatusLift.finish:
            # house.lift.attachment_floor(house.floors[0])
            break
    pass
