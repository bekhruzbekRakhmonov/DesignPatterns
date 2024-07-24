class FootballPlayer:
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Player name: {self.name}\nPlayer number: {self.number}\n"


    def start_playing(self,shoot):
        print(f"{self}{shoot.action()}")

class PlayFootball:
    def __str__(self):
        return "football started"

    def action(self):
        return "kick the ball"

class Football:
    def __init__(self,name,number):
        self.player_name = name
        self.player_number = number

    def create_player(self):
        return FootballPlayer(self.player_name,self.player_number)

    
    def shoot(self):
        return PlayFootball()

class VolleyballPlayer:
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"Player name: {self.name}\nPlayer number: {self.number}\n"


    def start_playing(self,shoot):
        print(f"{self}{shoot.action()}")

class PlayVolleyball:
    def __str__(self):
        return "volleyball started"

    def action(self):
        return "throw the ball"

class Volleyball:
    def __init__(self,name,number):
        self.player_name = name
        self.player_number = number

    def create_player(self):
        return VolleyballPlayer(self.player_name,self.player_number)

    
    def shoot(self):
        return PlayVolleyball()

class GameWorld:
    def __init__(self,factory):
        self.player = factory.create_player()
        self.shoot = factory.shoot()

    def play(self):
        self.player.start_playing(self.shoot)

def get_user_choice():
    try:
        user_choice = input("Enter a number: ")
        user_choice = int(user_choice)
        if user_choice < 3:
            return (user_choice,True)
        else:
            print("Invalid choice")
            return (user_choice,False)
    except ValueError:
        print("Please enter a number not string")
        return (user_choice,False)
    
def main():
    text = """
    Choose one of them: \n
    \t\t1.Football\n
    \t\t2.Volleyball\n
    """
    print(text)
    user_choice,valid = get_user_choice()

    while not valid:
        user_choice,valid = get_user_choice()

    if user_choice == 1:
        game = Football("Messi", 10)
    else:
        game = Volleyball("Ronaldo", 7)

    game_world = GameWorld(game)
    game_world.play()


if __name__ == "__main__":
    main()
