### Python Trail MVP Requirements

- Ask for user to choose number of players.

- Ask for user to name each player.

- Assign 5 trail options to each user's hand.

- Assign 5 supplies to each user's hand.

- Display a graphic for beginning of the game.

- Rotate through player turns:

  - Allow a player to choose a trail option from their hand OR randomly choose a trail option for them if they are out of trail options.
    - If a random trail option must be chosen, Roll the dice to determine choice.

  - Remove the chosen trail option from the player's hand

  - Notify the user of the consequence of chosen trail option.
    - Should display a graphic of consequence.

  - Calculate and implement the consequence of chosen trail option.

    - If the consequence of the chosen trail is a dice roll,
      - Roll the dice to determine outcome

      - Depending on the dice roll, allow the player to proceed, end the players turn, or kill the player.

    - If the consequence of the chosen trial is a calamity,
      - Add a random calamity to the player's hand

    - If the consequence of the chosen trail is nothing,
      - proceed

    - If the consequence of the chosen trail is a trail or supply
      - add the trail or supply to the player's hand

  - Allow a player to choose a supply from their hand, if they have supplies.

    - Remove the chosen supply from the player's hand if it's applicable to any calamities they have.  

      - Remove the applicable calamity from the player's hand

    - Provide an error message if the player chooses a supply that is not useful for any calamities in their hand.

  - Check the given calamities and determine if the player can live.

    - Kill the player if applicable

- Check for alive players.
  - If players are still alive, continue player turns until 20 trail options have been played total.
    - If players play a total of 20 trail options, they have won the game.

  - If all players die, the game is over. They have lost.

- Display a graphic at the exit of the game
  - If game was won, display happy graphic
  - If game was lost, display evil graphic


### Functional Features

- Application will run on python 3.7+

- Application will run only on the command line - no GUI

- Application will show ascii graphics for most major events

- Application should be able to add features.

  - First feature updates:
    - Allow players to use supplies from each other's hands
    - Allow calamities to keep track of turns and kill the player if a certain number of turns has completed before removing the calamity.
    - Allow players to resolve calamities for other players
