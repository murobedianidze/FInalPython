import random
import time
from functions import GameFunctions
from data import country_capitals
from leaderboard import Leaderboard
class Game:
    def __init__(self):
        self.functions = GameFunctions()
        self.leaderboard = Leaderboard('leaderboard.txt')

    def game_over(self):
        print("You've given 3 wrong answers. Game Over!")
    def play_game(self):
        player_name = input("Enter your name: ")
        countries = list(country_capitals.keys())
        random.shuffle(countries)
        score = 0
        correct_answers = 0
        start_time = time.time()
        guess_attempts = 0
        wrong_answers = 0

        for country in countries:
            capital = country_capitals[country]
            self.functions.clear_screen()
            self.functions.display_question(country)

            guess_attempts = 0
            while guess_attempts < 1:
                guess = self.functions.get_user_input()
                if self.functions.check_user_input(guess, country, capital):
                    self.score += 1
                    self.correct_answers += 1
                    break
                else:
                    guess_attempts += 1
                    wrong_answers += 1
                    if wrong_answers == 3: 
                        self.game_over()
                        return score, correct_answers
                    if guess_attempts == 3:
                        self.functions.display_correct_answer(country, capital)
                        break

        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        self.functions.display_score(score, time_taken)
        self.leaderboard.update_scores(player_name, score, time_taken, correct_answers)
        self.leaderboard.display_leaderboard()

if __name__ == "__main__":
    game = Game()
    while True:
        game.play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            game.leaderboard.save_scores()
            print("Thanks for playing!")
            break
