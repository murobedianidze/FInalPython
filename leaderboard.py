class Leaderboard:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.scores = self.load_scores()

    def load_scores(self):
        try:
            with open(self.file_path, 'r') as file:
                scores = [line.strip().split(',') for line in file.readlines()]
                return sorted(scores, key=lambda x: int(x[1]), reverse=True)
        except FileNotFoundError:
            return []

    def update_scores(self, player_name, score, time_taken, correct_answers):
        self.scores.append([player_name, str(score), str(time_taken), str(correct_answers)])
        self.scores = sorted(self.scores, key=lambda x: int(x[1]), reverse=True)[:10]

    def save_scores(self):
        with open(self.file_path, 'w') as file:
            for score in self.scores:
                file.write(','.join(score) + '\n')

    def display_leaderboard(self):
        print("\nLEADERBOARD\n")
        print("{:<15} {:<10} {:<10} {:<15}".format("Player", "Score", "Time (s)", "Correct Answers"))
        for score in self.scores:
            print("{:<15} {:<10} {:<10} {:<15}".format(score[0], score[1], score[2], score[3]))