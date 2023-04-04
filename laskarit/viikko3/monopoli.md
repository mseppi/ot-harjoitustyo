```mermaid
classDiagram
    Board"1" -- "40"Square
    Player "2-8" -- "*" Board
    Player "1" -- "1" Square
    Player..>Dices
    Square"next square" -- Square
    Square..>Cards
    Cards--Player
    Building--Player
    Action--Cards
    Action--Player
    Building--Square
    class Player{
    money
    ownerships
    }
    class Board    
    class Square{
    start
    prison
    chance
    community chest
    train station
    street
    }
    class Dices{
    digit
    }
    class Cards{
    chance
    community chest
    }
    class Action
    class Building{
    house
    hotel
    }
    
