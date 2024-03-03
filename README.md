# Medieval Hangman

This is my third milestone project which is a game Medieval Hangman. This game has been designed for those interested in trying a bit of their knowledge around medieval Europe, battles to be specific.
Rules has and tips been added inside the game. 

![View Deployed Site Here!](https://medieval-hangman-79561d9b2ff5.herokuapp.com/)

## How to play

Medieval Hangman is fairly simple game, you need to guess a medieval battle, as a hint it is mostly Towns/Citys around Europe as the game is based around European region.
Every correct guess would reveal a letter that has been guessed correctly while others would remain as underscores.
If players attempt count reaches 0 they will be hung and it will be game over.

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

## Testing

I have manualy tested this porject by:
- Passed code through PEP8 linter and found no issues
![Linter Results](documentation/validator.png)
- Entering same letters provides with you have tried this letter before.
- I have tried the game inside the Gitpod.io terminal as well as Heroku app terminal.

## Bugs remaining

    - If typing nothing while in game, game displays "Well done you guessed the letter" but, nothing besides that happens, player count remains the same guessed letter do not appear. Did not have enough time to solve this bug.

## Bugs solved

- I had issues with letters that have been guessed not prining out afer being typed in. In order to solve this I shifted print statements around which seems to done the trick.

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

## Aplications Used

Gitpod.io IDe for developing the website.
Github.com was used for keeping version control and posting my readme.
Heroku.com was used  for hosting website.
Code institute template for begining of work.
W3C schools for refreshing memories on code.
