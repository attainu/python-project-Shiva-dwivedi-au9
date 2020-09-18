# python-project-Shiva-dwivedi-au9
AttainU python project Repository

## Introduction
### Welcome to Snakes and Ladders Dice Game user documentation.
Snakes and Ladders, known originally as Moksha Patam, is an ancient Indian board game for two or more players regarded today as a worldwide classic. 
# Features
Snakes and Ladders is an ancient south Asian board game. Which consists 10 X 10 scored gridded board and some snakes and ladders spotted on board. 100 is the maximum and winning score. Once any player get to that score, immediately declared as winner.
## Following are the features available in this game:-
1. **SNAKE:** This game is customizable that is, you can choose the number of snakes you want on your board and also customize the position (head and tail of the snake) of the snake according to your convenience.
2. **LADDER:** You can choose the number of ladders as well as the position (start and the end of ladder) of your ladder as per the convenience.
3. **PLAYERS:** This game has two options as of now. You can play 2 players and 4 players game.
4. **DICE:** Has one dice and you can get values ranging from 1-6 depending on your luck!
5. **NO INFINITE LOOP:** As the snakes and ladders are inputted by the user so this game ensures that the user doesn’t enter a ladder such that it coincides with the snake (head of snake coinciding with the end of ladder and tail of snake with the start of the ladder) and ends up in infinite loop.


# How It Works
*	**Step 1:** Enter the number of players that is 2 0r 4.
*	**Step 2:** After entering the number of players you will get a welcome message and rules for playing the game.
*	**Step 3:** The code will work based on the number of players.
*	**Step 4:** The snakes and ladders are user inputted and are stored in a dictionary in the form of head as key, tail as the value to that key and similarly for the start and end of the ladder. 
*	**Step 5:** When you hit enter the dice value are shown randomly in the range   (1-6) and the value is added to player’s current position.
              Customized messages pop on your screen when you roll a dice , get bitten by a snake or climb a ladder.
* **Edge cases handled** – The code will take care of the inputs entered by the user like – 
     1. For Snake: Tail should be less than the head. 
     2. Two heads cannot be at the same position. 
     3. For Ladder: Start should be less than the end. 
     4. Two starts cannot be at the same position. 
     5. NO INFINITE LOOP: As the snakes and ladders are inputted by the user so this game ensures that the user doesn’t enter a ladder such that it coincides with the snake (head of snake coinciding with the end of ladder and tail of snake with the start of the ladder) and ends up in infinite loop.
     6. No. of snakes and ladder will be positive or else prompted.
     7. The ladder and snake positions will be in the range of (1-100)
*	**Step 6:** If the current position of a player reaches the key in the dictionary of snake or ladder, the player automatically moves to its value.
*	**Step 7:** Check for winner (whether current player scored 100 or not)
*	**Step 8:** If winner is not found it’s next player’s turn (will repeat step 5 and step 7)
*	**Step 9:** If winner found game is over and a message will prompt congratulating the winner.
