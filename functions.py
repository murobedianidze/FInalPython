import os

class GameFunctions:
    def display_score(self, score, time_taken):
        print(f"Your score: {score}")
        print(f"Time taken: {time_taken} seconds")

    def display_correct_answer(self, country, capital):
        print(f"The correct answer was {country}. Capital: {capital}")

    def display_question(self, country):
        print(f"What is the capital of {country}?")

    def get_user_input(self):
        return input("Enter your answer: ").strip()

    def check_user_input(self, guess, country, capital):
        if guess.lower() == capital.lower():
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
