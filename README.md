# Exotic Fruits Quiz

## UX

This web application is made for those who like to do quizzes for entertainment or to test their knowledge on what the quiz's topic is. My target market could more specifically
include students within the Food Technology sector who wish to test their knowledge on exotic fruits, teachers who wish to test these students, or people who just enjoy taking
random quizzes for their own enjoyment. This type of user will want to be able to enter a unique username, be presented with questions and be given an input area for their answer.
This user will also want to be able to view their score once they have completed the quiz and compare it to other player's scores, with the choice to restart the quiz. 
My project is a suitable way of achieving this because it provides a form for the user to use when they want to choose a unique username, fifteen images of exotic fruits and a form
for each image whereby the user may guess the name for each fruit. Once they have completed the quiz, a highscores table will be presented with the top ten scores and the user can choose 
to replay the quiz if they would like to achieve a higher score. The brief requires the web application to allow multiple users to do the quiz at the same time - my project allows this
and each player's name and score can be stored at the same time, even if users are using different browsers.

General User Stories:

- As a user type, I want to be able to enter a unique username and proceed to start the quiz.
- As a user type, I would like to be able to find out how to play the quiz.
- As a user type, I would like to compare my final score with other scores.
- As a user type, I would like to be able to play the quiz at the same time as other users.

Real Life User Stories:

- User 1: I'd like my username to be PianoMan123.
- User 2: I would like there to be a set of instructions on how to play the quiz.
- User 3: I would like to see if I beat PianoMan123 on a highscores table.
- User 4: I would like to be able to play at the same time as PianoMan123 and PizzaMan456.

Wireframes:

The mockups for Desktop, Tablet and Mobile view can be found in /documentation/mockups. These have been made through Balsamiq Mockups 3. 

A more detailed documentation of the Five Planes of UX is available [here](documentation/ux_planes.pdf).

## Features

- Username input field - allowing user to enter a unique username
- Start button - allowing user to proceed to the quiz
- Instructions - allowing user to find out how to do the quiz before they start
- Answer input field - allowing user to enter their answer/guess, followed by submit, skip or restart quiz buttons
- Score - allowing user to see their score whilst they play the quiz
- Incorrect guesses - allowing user to see their incorrect guesses as well as previous player's incorrect guesses
- Highscores table - allowing users to compare their scores with each other, also giving user the option to replay the quiz

### Existing Features

- Username input field and start button allows Users 1 to enter their unique username of 'PianoMan123' at the same time on a different browser as another user, and to proceed to the quiz.
- Instructions feature enables User 2 to find out how to play the quiz.
- Answer input field allows Users 1, 2, 3 and 4 to enter and submit their own guesses.
- Incorrect guesses allows Users 1, 2, 3 and 4 to see which incorrect guesses have been entered by a particular user, e.g. User 2 could see User 4's incorrect guess. An issue with this is that the quiz page would need to be refreshed regularly if users would like to see other's incorrect guesses in real time. 
- Score feature allows Users 1, 2, 3 and 4 to see their scores (with a maximum of 60).
- Highscores feature allows User 3 to see if they beat 'PianoMan123' or any other player that has completed the quiz.
- The quiz as a whole allows User 4 to play the quiz at the same time as 'PianoMan123' and 'PizzaMan456'.

## Testing

Automated testing has been completed with the unit testing framework (unittest). I carried out six tests:

- test_write_name
- test_update_score
- test_update_guess
- test_get_guesses
- test_check_answer
- test_get_scores

All of these tests passed when the [test_quiz.py](test_quiz.py) file was run. 

User stories have been manually tested with different scenarios that the player may experience during their visit to the web application.

1. Username form:
    1. Go to the username input box
    2. Try to press "Let's go!" without entering a username and verify a warning is prompted
    2. Enter a unique username with a variety of special characters
    3. Press "Let's Go!" to begin

2. Answer form:
    1. Enter a random guess and verify that an incorrect guess is displayed below the quiz and the current score is decremented by 5 points
    2. Enter an empty input field and verify that an empty incorrect guess is displayed below the quiz and the current score is decremented by 5 points
    3. Enter the correct answer and verify that 5 points are added to the current score
    4. Skip a question and verify that 2 points are deducted from the current score
    5. Press "Restart Quiz" and verify that the user is redirected to the index page

