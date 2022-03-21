{% include navigation.html %}

## Daniel Levy's Boomin' Battleship
### What is Battleship?
Battleship is a guessing game, where battleships are marked on each person's board on a grid, from A-J horizontally and 1-10 vertically. The battleships are placed on each person's board in secret, and the ships are not allowed to overlap. The players call points on the grid, letter-first and number-second, to try to hit the opponent's battleship. If the battleship is hit, the opponent says that it is hit.

### Written Portion
3a. The overall purpose of the program is to replicate a game of Battleship. The user tries to take down the AI's ships, while the AI attacks at random positions. The user is given five different ships on the gray "dock." The user has the ability to rotate each ship and place it anywhere on the boundaries of the blue box. Meanwhile, the AI's ships are hidden. The user starts the game by hitting "Start Game". When a ship is sunk, it displays what type of ship sunk, and whose side it belongs to. The user hits a ship by clicking anywhere on the pink box: a hit displays a red square, whereas a miss displays a blue square. Once a player finishes their turn, the AI attacks at a random position, with the same parameters applied. Once a side wins by taking down all the opponent's ships, a text will display which side won.

3b. 


![image](https://user-images.githubusercontent.com/89277619/155940941-fcb394bd-644c-47b0-a3ad-d13c63ea19aa.png)


This portion of code displays how each hit in the game is stored. A square indicating that a ship is hit, stored as the name "Boom", then indicates what type of ship was hit. A missed shot stores the variable "Miss."


![image](https://user-images.githubusercontent.com/89277619/155941626-df9cea9a-19b3-49c6-8830-f58b01b69a8f.png)


This portion of code displays what happens to the enemy ship if all tiles that consist a certain ship are sunk. When the user has sunk all tiles of that ship, it is stored in the list as "sunk" and cannot be hit again.

The name of the list being used in the code is known as "revealSquare."

The data variables in that list contain the number of tiles of each ship, how each ship sinks, as well as the displayed message when each ship is sunk. 

The list manages complexity in the program in the sense that it displays what type of ship is hit as well as the message should an entire ship be hit. If the list were not used, the tiles hit on each enemy ship would not be counted. and thus not display a hit or a sunken ship.

3c. 
![image](https://user-images.githubusercontent.com/89277619/155946454-bbf78af5-dede-4c49-b644-e22648671ba6.png)

The first program code segment contains the parameter if either the user or the AI wins. It has an effect on the functionality of the procedure in the sense that the winner is returned and displayed, and that neither the user nor the AI can hit each other after the game is over. 

![image](https://user-images.githubusercontent.com/89277619/155946540-cc8f58e0-04d7-45bb-a9ea-18648fdbfd0e.png)

The second code is sequenced so that when every ship is hit on either side, it displays whether the user or the AI has won. Once either side has won, the win is set as true, and each side continues to play until either side has won. Once a side has won, the function displaying a winner is called. 

The identified procedure is crucial to the program in the sense that if it is not implemented, the user or the AI will have the ability to continue playing, even when one side has technically won. 

The function checks for wins under the function checkForWins(). Each ship is worth ten points when it is sunk. When all five ships have sunk on either side, and thus fifty points have been won, the winner is displayed, isGameOver is set to be true, and neither the User nor AI cannot place another square.

3d. 
The first call to the procedure is shown in the function revealSquare. When a ship is hit, the hit count for that ship is increased by one. The condition is tested when a tile is hit on either side, the function is called, displaying whether the square selected was a hit or miss under the name "Boom" or "Miss" respectively. If the square hits a ship tile, it is then counted as a hit in the program, and the hit is then displayed as a red square. Similarly, when the square hits the "water", or misses one of the ships, it is displayed as a blue square.

The second call to the procedure is the function determining win. Each ship is designated ten points that is added to either side when a ship is hit. Once that side reaches fifty points, the game is over. The condition tested by the second call is if those fifty points are reached. Until all points are reached by one side, the game will continue and isGameOver is set to false. Once a side has reached 50 points and isGameOver is set to be true, the game ends, and neither side can place a square.
### Code Video
https://www.youtube.com/watch?v=E2aT87cMPho
