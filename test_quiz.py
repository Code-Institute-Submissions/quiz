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

if __name__ == "__main__":
    unittest.main()