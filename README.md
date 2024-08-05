# Medieval Hangman

This is my third milestone project which is a game Medieval Hangman. This game has been designed for those interested in trying a bit of their knowledge around medieval Europe, battles to be specific.
Rules has and tips been added inside the game. 

View Deployed Site Here!(https://medieval-hangman-79561d9b2ff5.herokuapp.com/)

## How to play

Medieval Hangman is fairly simple game, you need to guess a medieval battle, as a hint it is mostly Towns/Citys around Europe as the game is based around European region.
Every correct guess would reveal a letter that has been guessed correctly while others would remain as underscores.If players attempt count reaches 0 they will be hung and it will be game over.

## User experience(UX)

- ### User Stories

    #### As a User, I want to be able to:
   
    1. Understand how to play the game.
    2. Be able to read rules and tips if I haven't played the game before.
    3. See the amount of attempts left before the game ends.
    4. See the amount of letters inside the secret word.
    5. If I fail to guess the word to see what the secret word was.


## Existing features

- Random word generation - Picks out a word to be guessed from a list provided.
- Player can only see underscores and count how many letters could be added.
- Accepts user input.
- Limited amount of attempts per round.
- If same letter guessed twice, game will return with "You have tried this already!"

## Future features

- Add option for different regions around the world for more tests of knowledge.
- Give hints about where the battle took place or who were the commanders.
- In general add more battles as the current sample list is quite small.
- Add option for different centuries.
- Add option for resuming games or quitting.



## Testing

| Test label              | Test action                                  | Expected outcome                                                                                                                                                                                                   | Test outcome |
| ----------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| Enter Name              | Run program                                  | Display message to enter players name.                                                                                                                                                                             | Pass         |
| Blank Name              | Leave name section empty                     | If user leaves their name as blank it should come up as "Anonymous Player".                                                                                                                                        | Pass         |
| Display welcome Message | Enter name or leave it blank and press enter | After user enters their name or leaves it blank they should receive a welcome message and a display of rules of hangman as well as tips on how to play.                                                            | Pass         |
| Continue                | Type y or n in terminal to proceed           | After pressing y user should be able to proceed. If they chose "n" they will be brought back to beginning.                                                                                                         | Pass         |
| Display Word            | Press Enter                                  | After user has pressed enter on their keyboard. User will be displayed with their word which will be covered with "_" on every letter that is to be guessed.                                                       | Pass         |
| Correct Guess           | Enter correct letter                         | If user guesses correct letter, the hidden letter will be revealed while the rest of the unguessed letters remain the same. In addition they will receive a message "Well done! you have guessed correct letter!". | Pass         |
| Incorrect Guess         | Enter incorrect letter                       | If user guessed incorrectly their remaining attempts will go down by 1 until they reach 0 attempts. They also are displayed with message: "You are incorrect!".                                                    | Pass         |
| Invalid Guess           | Enter number/multiple letters                | If user enters numbers or multiple letter they will be receive a following statement "Please enter a letter" or "Please enter one letter". Their remaining attempts won't change.                                  | Pass         |
| Winning                 | Guess the word correctly                     | If user guessed all the letters correctly they be displayed a message "Congratulations! You have guessed the word:(The word guessed) ".                                                                            | Pass         |
| Loosing                 | Guess the word incorrectly                   | If user ran out of attempts they will receive a message: "You've ran out of attempts! You word was:(The correct word) "                                                                                            | Pass         |

- I have manualy tested this porject by:
- Passing code through PEP8 linter and found no issues
![Linter Results](documentation/validator.png)

- I have tried the game inside the Gitpod.io terminal as well as Heroku app terminal.

## Bugs remaining

- Currently there are no known bugs.

## Bugs solved

- I had issues with letters that have been guessed not prining out afer being typed in. In order to solve this I shifted print statements around which seems to done the trick.

- Some words were being displayed altogether due to missing commas after battle names.

## Deployment

# Github forking

- Go to github repository
- At the top of the page you will find  a "Fork Button" press it.
- In the next page you will find green button in middle of your page, again click create.

# Heroku Deployment

- Log into Heroku.
- Inside the app click on dashboard, then click on "Create new App".
- Enter Unique name for you application otherwise it might get rejected, select region which suits you.
- Click on create app.
- At the application configuration page, apply settings as follow Deploy section: aplication. In the reveal Config VARS enter "CREDS" for the Key you want to paste your contents from your CREDS.json file. Note that this step is neccesary if you have added external APIs.
- Click on add.
- Add another config Var  with key PORT and value of "8000"
- Inside  Settings go down to the Buildpack  while clicking on Add Build Pack.
- Make sure to add python as first and then nodejs in order to run server properly.
- Go to the Deploy Section and select  to deploy "Automatically"(Note this is not necessary but saves time, as your app will automatically refresh with every git push)
- Click on deploy wait for deploy ment website should be will be displayed there.

## Credits

 1. Gitpod.io IDe for developing the website.
 2. Github.com was used for keeping version control and posting my readme.
 3. Heroku.com was used  for hosting website.
 4. Code institute template for beginning of work.
 5. W3C schools for refreshing memories on code.
 6. https://pep8ci.herokuapp.com/ Python Linter

