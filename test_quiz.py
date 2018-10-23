import unittest
import quiz

class TestQuiz(unittest.TestCase):
    
    # Test if write_name writes the player's name to players.txt
    def test_write_name(self):
        username = "Player123"
        quiz.write_to_file("data/players.txt", username + "\n")
        content = open("data/players.txt").read()
        self.assertIn("Player123", content)
        #delete test username after use.
        with open("data/players.txt", "r+") as players:
            player = players.readlines()
            players.seek(0)
            for line in player:
                if line != "Player123" + "\n":
                    players.write(line)
            players.truncate()
            players.close()
     
    # Test if score and username are updated when update_score function called        
    def test_update_score(self):
        username = "Player123"
        score = 10
        quiz.update_score(username, score)
        content = open("data/scores.txt").read()
        self.assertIn("{0} - {1}".format(username, score), content)
            
        # Delete Player123 from scores.txt file
        with open("data/scores.txt", "r+") as player_data:
            players = player_data.readlines()
            player_data.seek(0)
            for line in players:
                if line != "Player123, 10" + "\n":
                    player_data.write(line)
            player_data.truncate()
            player_data.close()
            
    # Test if guess is stored when update_guess function called
    def test_update_guess(self):
        username = "Player123"
        guess = "guess"
        quiz.update_guess(username, guess)
        content = open("data/guesses.txt").read()
        self.assertIn("{0} - {1}\n".format(username, guess), content)
        
        # Delete test guesses 
        with open("data/guesses.txt", "r+") as guess_data:
            guess = guess_data.readlines()
            guess_data.seek(0)
            for line in guess:
                if line != "Player123 - guess" + "\n":
                    guess_data.write(line)
            guess_data.truncate()
            guess_data.close()
            
    # Test if get_guesses returns 10 or less incorrect guesses
    def test_get_guesses(self):
        d_guesses = quiz.get_guesses()
        self.assertTrue(len(d_guesses) <= 10)
        print("expected <= 10, got", len(d_guesses))


if __name__ == "__main__":
    unittest.main()