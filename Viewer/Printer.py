class LiftPrinter:

    @staticmethod
    def pr_selected_error(message):
        print(f'Этаж {message['target']} не существует')

    @staticmethod
    def pr_current(message):
        print(f'Текущий этаж {message['current']}')

    @staticmethod
    def pr_done(message):
        print(f'{message['name']} приехал')

    @staticmethod
    def pr_selected(message):
        print(f'Выбран этаж {message['target']}', end=', ')

    @staticmethod
    def pr_move_to_down(message):
        print(f'едем вниз')

    @staticmethod
    def pr_move_to_up(message):
        print(f'едем вверх')

    @staticmethod
    def pr_summon(message):
        print(f'{message['name']} на {message['current']} Вызываем {message['name']} на {message['target']} этаж', end=', ')


class DoorPrinter:
    @staticmethod
    def pr_open(message):
        print(f'{message} открыты')

    @staticmethod
    def pr_close(message):
        print(f'{message} закрыты')

    @staticmethod
    def pr_opening(message):
        print(f'Открываются {message}')

    @staticmethod
    def pr_closing(message):
        print(f'Закрываются {message}')


class FloorPrinter:
    pass


class HousePrinter:
    pass


class ObjPrinter:
    pass
