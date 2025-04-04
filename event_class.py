class Event:
    def __init__(self, description, graphics, choices):
        self.description = description
        self.graphics = graphics
        self.choices = choices

    def display(self, player):
        print("\n" + self.description)

        if not self.choices:
            print("\nGame Over.")
            return None
        
        # Convert choices into a numbered list
        choice_list = list(self.choices.keys())
        choice_map = {str(i + 1): choice_list[i] for i in range(len(choice_list))}

        # If there's a graphic
        if self.graphics is not None:
            with open("graphics/" + self.graphics, "r", encoding="utf-8") as file:
                print(file.read())
            

        print("\nMitä teet?")
        for number, choice in choice_map.items():
            print(f"{number}. {choice}")

        while True:
            user_input = input("> ").strip().lower()
            
            # Check if input is a valid number
            if user_input in choice_map:
                user_input = choice_map[user_input]  # Convert number to actual choice text
            
            if user_input in self.choices:
                choice_data = self.choices[user_input]
                
                # If there's a happening
                if "happening" in choice_data:
                    for stat, change in choice_data["happening"].items():
                        player.modify_stat(stat, change)

                # If there's a skill check
                if "skill_check" in choice_data:
                    stat, difficulty = choice_data["skill_check"]
                    if player.skill_check(stat, difficulty):
                        print("Onnistuminen!")
                        if "success_outcome" in choice_data:
                            for stat, change in choice_data["success_outcome"].items():
                                player.modify_stat(stat, change)
                        if "success_event" in choice_data:
                            return choice_data["success_event"]
                    else:
                        print("Epäonnistuminen!")
                        if "fail_outcome" in choice_data:
                            for stat, change in choice_data["fail_outcome"].items():
                                player.modify_stat(stat, change)
                        if "fail_event" in choice_data:
                            return choice_data["fail_event"]
                
                return choice_data["next_event"]
            elif user_input == "poistu":
                print("Poistu pelistä.")
                return None
            elif user_input == "apua":
                print("Komennot:")
                for choice in self.choices:
                    print(f"- {choice}")
                print("- Kirjoita valinta, jonka haluat tehdä.")
                print("- Kirjoita 'poistu' poistuaksesi pelistä.")
                print("- Kirjoita 'apua' nähdäksesi tämän viestin uudelleen.")
            else:
                print("Virheellinen valinta. Yritä uudelleen. Kirjoita 'apua' nähdäksesi vaihtoehdot.")