from warrior import Warrior

API_KEY = "AIzaSyBO4vjZjodHXbmIGjf4B2ZuXGZcYudiips"
URL = "https://maps.googleapis.com/maps/api/geocode/json"

power_warrior = Warrior("Power man", 15, 1.0, 100)
healthy_warrior = Warrior("Healthy man", 10, 1.0, 150)
skill_warrior = Warrior("Skill man", 10, 1.5, 100)

warriors = [power_warrior, healthy_warrior, skill_warrior]

win_message = "YOU ARE WINER"
losing_message = "YOU LOSE"