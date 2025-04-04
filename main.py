from player_class import Player
from events import events

def play_game():
    player = Player()
    current_event = "start"

    while current_event:
        event = events[current_event]
        current_event = event.display(player)
    
    player.display_stats()
    print("Kiitos pelaamisesta!")

if __name__ == "__main__":
    with open("flashscreen.txt", "r", encoding="utf-8") as file:
        print(file.read())
    play_game()