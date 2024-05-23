from Model.Floor import Floor
from Model.Lift import Lift


class House:
    def __init__(self, height, max_of_floors):
        self.maxOfFloors = max_of_floors
        self.height = height
        self.lift = Lift(self.height, 20)
        self.floors = []
        self.floors.append(Floor(Number=1, lift=self.lift))
        self.lift.attachment_floor(self.floors[len(self.floors)-1])
        for i in range(2, self.maxOfFloors + 1):
            self.floors.append(Floor(Number=i, lift=self.lift))
            count = len(self.floors) - 1
            parent = self.floors[count - 1]
            current = self.floors[count]
            current.attachment_parent(parent)
            parent.attachment_child(current)
        print(f'В доме {len(self.floors)} этажей')

    def viewer_of_floors(self):
        pass


if __name__ == '__main__':
    house = House(height=400, max_of_floors=10)
    house.floors[9].summon_lift()
    while True:
        if house.lift.update():
            house.lift.attachment_floor(house.floors[9])
            break
    house.lift.go_to_floor(1)
    while True:
        if house.lift.update():
            house.lift.attachment_floor(house.floors[0])
            break
    pass
