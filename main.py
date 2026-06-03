
leaderboard = []


def start():
    while True:
        func = input("What do you wana do? Ad name or retrieve leaderbord? adn/wlead ")
        if func == "adn":
            add_name = input("Add name: ")
            add_time = input(f"Add time of {add_name}: ")

            runner = {
                "name": add_name,
                "time": add_time
            }

            leaderboard.append(runner)
        elif func == "wlead":
            for runner in leaderboard:
                print(runner["name"], runner["time"])
            
                             
                             
print("Welcome to TimeRank")
print("Made by TimFloClausen")

enter = input("Press enter to start! ")
start()


