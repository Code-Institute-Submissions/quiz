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

### Features Left to Implement
- Shuffle feature - shuffles all of the images of exotic fruits each time the quiz is restarted, making the quiz more challenging
- Hints feature - the player could have the chance to view a hint, however, this takes away a point from the player's current score. This could make the quiz easier to complete.

## Technologies Used

- HTML
    - This project uses **HTML** to build the foundation of the web application and include links to Bootstrap, Bootstrap JS, CSS, and Font Awesome.
- CSS
    - This project uses **CSS** to style the features of the web application, including the header, footer and each page of the quiz.
- [Python](https://www.python.org/)
    - This project uses **Python** to provide the backend functionality of the quiz, and also to run automated tests for the application. 
- [JSON](https://www.json.org/)
    - This project uses **JSON** to provide the core data for the quiz, including exotic fruits images and names.
- [Flask](http://flask.pocoo.org/)
    - This project uses the **Flask** microframework to bring the frontend and backend of the application together.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** which is included with Bootstrap to allow for a dropdown menu to occur for mobile and tablet users. 
- [Bootstrap 4](https://getbootstrap.com/)
    - This project uses **Bootstrap 4** in order to apply columns, a navbar, a footer and to justify content within each page for a clean, fresh look. It is also used to implement a mobile-first approach and to aim for responsive design.
- [Bootswatch](https://bootswatch.com/united/)
    - This project uses the **Bootswatch Journal Theme** to apply the navbar within the header, and also to set the colour scheme of the website.
- [Font Awesome](https://fontawesome.com/)
    - This project uses **Font Awesome** to provide icons for the quiz buttons in the main quiz page and for 'Home' and 'Highscores' in the header for each page.
- [Balsamiq Mockups 3](https://balsamiq.com/)
    - This project uses **Balsamiq Mockups 3** for the Skeleton and Surface Plan, providing desktop, tablet and mobile views of the web application.
- [Google Fonts](https://fonts.google.com/)
    - This project uses **Google Fonts** to provide the 'Boogaloo' and 'Oswald' fonts for the headings of the web application.

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

This web application has been tested for responsiveness on different device screen sizes with the Chrome Developer Tools and Firefox Developer Tools.
There have been issues with the centering of content on mobile devices in both portrat and landscape, however, these have been fixed with the rearrangement of Bootstrap's columns and using media queries for specific devices, such as the iPad Pro and the Nexus 10. 

HTML and CSS code has been passed through the W3C Markup Validation Service. The HTML results brought back multiple errors, however, this is due to the url_for module in Python. The CSS code passed.


## Deployment

To run this application locally, you will need to clone or download the repository [here](https://github.com/kimpea/quiz) into a local IDE.
Check for any dependencies which are required for the application to run, e.g. Flask. This can be done by checking the requirements.txt file. 
Run the run.py file and click to view in a browser of your choice. Otherwise, the application can be viewed [here](https://python-quiz.herokuapp.com/).

For version control, this project was pushed to GitHub [here](https://github.com/kimpea/quiz).
This project has been deployed to [Heroku](https://python-quiz.herokuapp.com/). Config vars for heroku are:
- IP - 0.0.0.0
- PORT - 5000

Differences between development version and deployment version include fixing stray tags and updating the README.

## Credits and Acknowledgements

- I would like to credit Stack Overflow for helping me fix all of the bugs within the application, and I would also like to credit the Code Institute Practical Python lessons.

### Media

- The photos used in this site are obtained from the following links:
    - [Cherimoya](https://www.finecooking.com/ingredient/cherimoyas)
    - [Cucamelon](https://www.amazon.com/15-Cucamelon-Seeds-Watermelon-Melothria/dp/B071SG2FF2)
    - [Dragon Fruit](https://www.rachaelraymag.com/food/how-to-make-the-most-of-dragonfruit-season)
    - [Durian](https://www.indiamart.com/proddetail/durian-fruit-12676665430.html)
    - [Feijoa](https://www.healthyfood.co.nz/healthy-shopping/in-season-late-autumn-feijoas)
    - [Figs](https://www.exoticfruitsusa.com/best-place-to-buy-fresh-figs-p/brown20figs.html)
    - [Guava](https://timesofoman.com/article/139766)
    - [Jackfruit](https://www.fruitpassion.ch/en/product/jackfruit/)
    - [Kiwano](https://www.eatme.eu/products/kiwano)
    - [Kumquat](https://www.fourwindsgrowers.com/products/nagami-kumquat-one-year-old-tree)
    - [Lychee](http://befreshcorp.net/product/lychee/)
    - [Mangostee](nhttps://www.indiamart.com/proddetail/mangosteen-12967149530.html)
    - [Papaya](https://hirts.com/tainung-papaya-tree-carica-papaya-easy-to-grow-fruit-4-pot/)
    - [Rambutan](https://www.cfgastro.de/wp-content/themes/cfgastro/images//2016/10/03_Exoten.pdf)
    - [Tamarillo](https://www.exoticfruitmarket.net/Tamarillo-Fruit-Where-can-I-buy-Tamarillo-p/tamarillo6.html)
    - [Background Image](https://wallpaperscraft.com/tag/fruit/downloads)