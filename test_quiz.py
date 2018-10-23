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

if __name__ == "__main__":
    unittest.main()