import random

class Player:
    def __init__(self):
        self.stats = {
            "älykkyys": 0,
            "yleiskunto": 0,
            "karisma": 0,
            "wappufiilis": 0
        }
    
    def modify_stat(self, stat, amount):
        if stat in self.stats:
            self.stats[stat] += amount
            print(f"{stat.capitalize()}si on nyt {self.stats[stat]}.")

    def skill_check(self, stat, difficulty):
        """Returns True if the player passes the skill check, False otherwise"""
        roll = random.randint(1, 10) + self.stats.get(stat, 0)
        print(f"Heitetään {stat}... (Heitto: {roll}, Vaikeus: {difficulty})")
        return roll >= difficulty
    
    def display_stats(self):
        print("\nPelaajan tilastot:")
        for stat, value in self.stats.items():
            print(f"{stat.capitalize()}: {value}")