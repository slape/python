### Use Cases
Begin Game:
  - [Player] 1 chooses the total number of players
  - Player 1 enters their user name
  - Player's 2-4 enter their user names
  - Game creates list of players
  - Game shows welcome screen and opening graphic

Trail Choice:
  - Game displays user [trail] options
  - Player chooses a trial option
  - Game notifies the user of trail consequence or reward
  - Game implements consequence or reward

Trail Outcome:
  - Good Outcomes
    - Reward 2 Supplies
    - Reward 1 Supply
    - Remove 1 Calamity
    - End Turn
  - Bad Outcomes
    - Death
    - Loose 1 supply
    - Receive 1 calamity

Calamity/Supply:
  - Game assigns a [calamity] to a player
  - Game allows player to use a [supply] to resolve calamity
  - Game checks if calamity was resolved
  - Game [notifies] the user of calamity consequence or reward
  - Game implements [consequence] or [reward]

Calamity outcomes:
  - Good outcomes:
    - End Turn
    - Reward 1 supply
  - Bad outcomes:
    - Single Death
    - Group Death

Dice Engine:
  - Roll dice to determine trail Outcome
    - Roll and Even Number to continue turn.
    - Roll a 1 and player dies
    - Roll a 3 or 5 and player ends turn early. Player returns to same scenario next turn.
    - Roll and odd number and player loses a supply


Supply Engine
  - Use supply to resolve calamity
    - Use mace to resolve dino
    - Use pizza to resolve peyote trip
    - Use birthday cake to resolve starving
    - Use dress to resolve terminator
    - Use bullets to resolve fractal snake
    - Use dream_catcher to resolve treason
    - Use oxen to resolve steam mobile
    - Use keg to resolve hypothermia
    - Use spare parts to resolve flat tire
    - Use oxen to resolve dead oxen
    - Use vicodin to resolve measles

Death Engine
  - Kills Player
  - Notifies player of death:
    - Died by drowning
    - Kenny Killed you
    - Died from starvation
    - Died of heat stroke
    - God Killed you
    - Terminator Killed you
    - Fractal Snake Killed you
    - Drug overdose
    - Other members killed you for treason
    - Died of Hypothermia
    - Died of Dysentery
    - Died of Measles

### Potential Objects
  - [Player] -> [trail] -> [consequence]
  - [calamity] <-> [consequence] <-> [reward]
  - [calamity] <-> [Player] <-> [supply]
