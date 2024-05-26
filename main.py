
from Model.House import House
from Model.Status import StatusDoor, StatusLift


def check(floor):
    try:
        floor = int(floor)
        if not 0 < floor <= 10:
            print("Неверный номер этажа!")
            exit()
    except TypeError:
        print("Вы ввели не число!")
        exit()
    return floor


# Тест
if __name__ == '__main__':
    house = House(height=400, max_of_floors=10)
    while True:
        input_floor = check(input("На каком этаже вы находитесь? Введиите число от 1 до 10: "))

        using = house.floors[input_floor - 1].get_actions_for_user()
        for i in using:
            i['summon']()
        while True:
            house.lift.hendler.dispactch('update', None)
            if house.lift.door.status == StatusDoor.finish and house.lift.status == StatusLift.finish:
                house.lift.hendler.dispactch('update', None)
                # house.lift.attachment_floor(house.floors[9])
                break
        input_floor = check(input("На какой этаж отправимся? Введиите число от 1 до 10: "))
        house.lift.go_to_floor(input_floor)
        while True:
            house.lift.hendler.dispactch('update', None)
            if house.lift.door.status == StatusDoor.finish and house.lift.status == StatusLift.finish:
                # house.lift.attachment_floor(house.floors[0])
                break
        if input("Хотите выйти y/n: ") == 'y':
            break
    pass
