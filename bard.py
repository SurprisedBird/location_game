import constants


class Bard():
    text = "my text"
    def __init__(self):
        pass

    def warriors_info(self, warriors):
        print(f"Hello, yor have {len(warriors)} type of warriors")
        for warrior_number in range(len(warriors)):
            print(warriors[warrior_number].__dict__)

    def your_choose_print(self, player):
        print("You have choosen {}".format(player.name))

    def win_information(self, win):
        if win:
            print(constants.win_message)
        else:
            print(constants.losing_message)

