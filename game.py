from fight import Fight
from location import Location
import constants

class Game():

    fight = Fight()
    location = Location()

    location.get_coordinats(constants.URL, constants.API_KEY)
    location.get_location(constants.URL, constants.API_KEY)

    fight.print_hello(constants.warriors)
    fight.choose_warrior(constants.warriors)
    fight.choose_random_warrior(constants.warriors)
    fight.main_fight()

    win = fight.main_fight()
    if win:
        print(constants.win_message)
    else:
        print(constants.losing_message)